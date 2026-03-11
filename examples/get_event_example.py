import os

from dotenv import load_dotenv

import fingerprint_server_sdk
from fingerprint_server_sdk.configuration import Region
from fingerprint_server_sdk.rest import ApiException

load_dotenv()

# configure
region_str = os.environ.get('REGION', 'us').upper()
api_key = os.environ.get('PRIVATE_KEY')

if not api_key:
    print('API key not provided')
    exit(1)

configuration = fingerprint_server_sdk.Configuration(api_key=api_key, region=Region[region_str])

# create an instance
api_instance = fingerprint_server_sdk.FingerprintApi(configuration)
event_id = os.environ.get('EVENT_ID', None)
# RULESET_ID is optional. When provided, the response will include rule_action data.
ruleset_id = os.environ.get('RULESET_ID', None)

if not event_id:
    print('Event id not provided')
    exit(1)

try:
    event = api_instance.get_event(event_id, ruleset_id)
    print(f'Event ID: {event.event_id}')
    print(f'Timestamp: {event.timestamp}')
    if event.identification:
        print(f'Visitor ID: {event.identification.visitor_id}')
        print(f'Confidence: {event.identification.confidence.score}')
    if event.bot:
        print(f'Bot detection result: {event.bot}')
    if ruleset_id and event.rule_action:
        rule_action = event.rule_action.actual_instance
        print(f'Rule action: {rule_action.type}')
        if rule_action.type == 'block':
            print(f'Block with HTTP status code: `{rule_action.status_code}`')
            print(f'Block with response body: `{rule_action.body}`')
            print(f'Block with response headers: `{rule_action.headers}`')
        elif rule_action.type == 'allow':
            print(f'Allow with header modifications: `{rule_action.request_header_modifications}`')
except ApiException as e:
    print(f'Exception when calling get_event: {e}\n')
    exit(1)

print('\nGet event successful!')

exit(0)
