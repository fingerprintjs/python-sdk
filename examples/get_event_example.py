import os

import fingerprint_server_sdk
from fingerprint_server_sdk.configuration import Region
from fingerprint_server_sdk.rest import ApiException

from dotenv import load_dotenv

load_dotenv()

# configure
region_str = os.environ.get("REGION", "us").upper()
configuration = fingerprint_server_sdk.Configuration(
    api_key=os.environ["PRIVATE_KEY"], region=Region[region_str])

# create an instance
api_instance = fingerprint_server_sdk.FingerprintApi(configuration)
event_id = os.environ["EVENT_ID"]

try:
    event = api_instance.get_event(event_id)
    print(f"Event ID: {event.event_id}")
    print(f"Timestamp: {event.timestamp}")
    if event.identification:
        print(f"Visitor ID: {event.identification.visitor_id}")
        print(f"Confidence: {event.identification.confidence.score}")
    if event.bot:
        print(f"Bot detection result: {event.bot}")
except ApiException as e:
    print("Exception when calling get_event: %s\n" % e)
    exit(1)

print("\nGet event successful!")

exit(0)
