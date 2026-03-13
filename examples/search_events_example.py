import os
from datetime import datetime, timedelta, timezone

from dotenv import load_dotenv

import fingerprint_server_sdk
from fingerprint_server_sdk.configuration import Region
from fingerprint_server_sdk import ApiException

load_dotenv()

# configure
region_str = os.environ.get('REGION', 'us').upper()
configuration = fingerprint_server_sdk.Configuration(
    api_key=os.environ['PRIVATE_KEY'], region=Region[region_str]
)

# create an instance
api_instance = fingerprint_server_sdk.FingerprintApi(configuration)

end = datetime.now(tz=timezone.utc)
start = end - timedelta(days=7)
start_timestamp = int(start.timestamp() * 1000)
end_timestamp = int(end.timestamp() * 1000)

try:
    response = api_instance.search_events(limit=10, start=start_timestamp, end=end_timestamp)

    print(f'Found {len(response.events)} events')
    for event in response.events:
        event_visitor_id = event.identification.visitor_id if event.identification else '-'
        print(f'Event ID: {event.event_id}, Visitor ID: {event_visitor_id}')

    if response.pagination_key:
        print(f'Fetching next page with pagination_key: {response.pagination_key}')
        next_page = api_instance.search_events(
            limit=10,
            start=start_timestamp,
            end=end_timestamp,
            pagination_key=response.pagination_key,
        )
        print(f'Found {len(next_page.events)} more events on next page')

except ApiException as e:
    print(f'Exception when calling search_events: {e}')
    exit(1)

print('Search events successful!')

exit(0)
