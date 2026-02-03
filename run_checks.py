import os
import sys
from dataclasses import dataclass
from datetime import datetime, timedelta, timezone
from dotenv import load_dotenv
from typing import Tuple

from fingerprint_server_sdk import FingerprintApi, Configuration
from fingerprint_server_sdk.rest import ApiException

@dataclass(frozen=True)
class AppConfig:
    api_key: str
    region: str

def load_config() -> AppConfig:
    load_dotenv()
    api_key = os.getenv("PRIVATE_KEY")
    if not api_key:
        print("Error: PRIVATE_KEY environment variable not set", file=sys.stderr)
        sys.exit(1)
    region = (os.getenv("REGION") or "us").lower()
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
        first_event_identification_data = first_event.products.identification.data
        visitor_id = first_event_identification_data.visitor_id
        request_id = first_event_identification_data.request_id
        print("\n\n\nSearch events response: \n", search_events_response)
        search_events_response_second_page = api.search_events(2, start=start, end=end,
                                                                        pagination_key=search_events_response.pagination_key)

        if len(search_events_response_second_page.events) == 0:
            print("Second page of FingerprintApi.search_events: is empty", file=sys.stderr)
            return 1

    except ApiException as e:
        print("Exception when calling FingerprintApi.search_events: %s\n" % e, file=sys.stderr)
        return 1

    # Use existing visitor_id from FingerprintApi->search_events response to check FingerprintApi->get_visits method
    try:
        visits_response = api.get_visits(visitor_id, limit=2)
        print("\n\n\nVisits response: \n", visits_response)

    except ApiException as e:
        print("Exception when calling FingerprintApi.get_visits: %s\n" % e, file=sys.stderr)
        return 1

    # Use existing request_id from FingerprintApi->search_events response to check FingerprintApi->get_event method
    try:
        events_response = api.get_event(request_id)
        print("\n\n\nEvent response: \n", events_response.products)

    except ApiException as e:
        print("Exception when calling FingerprintApi.get_event: %s\n" % e, file=sys.stderr)
        return 1

    # Async methods examples
    try:
        visits_response_request = api.get_visits(visitor_id, limit=2, async_req=True)
        events_response_request = api.get_event(request_id, async_req=True)
        visits_response = visits_response_request.get()
        print("\n\n\nVisits async response: \n", visits_response)
        events_response = events_response_request.get()
        print("\n\n\nEvent async response: \n", events_response.products)
    except ApiException as e:
        print("Exception when calling Async example: %s\n" % e, file=sys.stderr)
        return 1

    # Check that old events are still match expected format
    try:
        search_events_response_old = api.search_events(1, start=start, end=end, reverse=True)
        if len(search_events_response_old.events) == 0:
            print("FingerprintApi.search_events: is empty for old events\n", file=sys.stderr)
            return 1
        old_event_identification_data = search_events_response_old.events[0].products.identification.data
        visitor_id_old = old_event_identification_data.visitor_id
        request_id_old = old_event_identification_data.request_id

        if request_id_old == request_id:
            print("Old events are identical to new\n", file=sys.stderr)
            return 1

        api.get_visits(visitor_id_old, limit=2)
        api.get_event(request_id_old)
        print("\n\n\nOld events are good\n")
    except ApiException as e:
        print("Exception when trying to read old data: %s\n" % e, file=sys.stderr)
        return 1

    print("Checks passed!")
    return 0

if __name__ == "__main__":
    sys.exit(main())
