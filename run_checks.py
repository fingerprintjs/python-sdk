import os
import sys
from dataclasses import dataclass
from datetime import datetime, timedelta, timezone
from dotenv import load_dotenv
from typing import Tuple

from fingerprint_server_sdk import FingerprintApi, Configuration
from fingerprint_server_sdk.configuration import Region
from fingerprint_server_sdk.rest import ApiException

@dataclass(frozen=True)
class AppConfig:
    api_key: str
    region: Region

def load_config() -> AppConfig:
    load_dotenv()
    api_key = os.getenv("PRIVATE_KEY")
    if not api_key:
        print("Error: PRIVATE_KEY environment variable not set", file=sys.stderr)
        sys.exit(1)
    region_str = (os.getenv("REGION") or "us").upper()
    region = Region[region_str]
    return AppConfig(api_key=api_key, region=region)

def make_client(cfg: AppConfig) -> FingerprintApi:
    configuration = Configuration(api_key=cfg.api_key, region=cfg.region)
    return FingerprintApi(configuration)

def create_range(days: int) -> Tuple[int, int]:
    end = datetime.now(tz=timezone.utc)
    start = end - timedelta(days=days)
    return int(start.timestamp() * 1000), int(end.timestamp() * 1000)

def main() -> int:
    cfg = load_config()
    api = make_client(cfg)

    start, end = create_range(90)

    # FingerprintApi->search_events usage example
    try:
        search_events_response = api.search_events(2, start=start, end=end)
        if len(search_events_response.events) == 0:
            print("FingerprintApi.search_events: is empty", file=sys.stderr)
            return 1
        first_event = search_events_response.events[0]
        visitor_id = first_event.identification.visitor_id
        event_id = first_event.event_id
        print("\n\n\nSearch events response: \n", search_events_response)
        search_events_response_second_page = api.search_events(2, start=start, end=end,
                                                                        pagination_key=search_events_response.pagination_key)

        if len(search_events_response_second_page.events) == 0:
            print("Second page of FingerprintApi.search_events: is empty", file=sys.stderr)
            return 1

    except ApiException as e:
        print("Exception when calling FingerprintApi.search_events: %s\n" % e, file=sys.stderr)
        return 1

    # Use existing event_id from FingerprintApi->search_events response to check get_event method
    try:
        event_response = api.get_event(event_id)
        print("\n\n\nEvent response: \n", event_response)

    except ApiException as e:
        print("Exception when calling FingerprintApi.get_event: %s\n" % e, file=sys.stderr)
        return 1

    # Check that old events are still match expected format
    try:
        search_events_response_old = api.search_events(1, start=start, end=end, reverse=True)
        if len(search_events_response_old.events) == 0:
            print("FingerprintApi.search_events: is empty for old events\n", file=sys.stderr)
            return 1
        old_event = search_events_response_old.events[0]
        event_id_old = old_event.event_id

        if event_id_old == event_id:
            print("Old events are identical to new\n", file=sys.stderr)
            return 1

        api.get_event(event_id_old)
        print("\n\n\nOld events are good\n")
    except ApiException as e:
        print("Exception when trying to read old data: %s\n" % e, file=sys.stderr)
        return 1

    print("Checks passed!")
    return 0

if __name__ == "__main__":
    sys.exit(main())
