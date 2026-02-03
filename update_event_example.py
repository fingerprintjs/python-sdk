import os
import argparse

import fingerprint_server_sdk
from fingerprint_server_sdk.rest import ApiException
from fingerprint_server_sdk.models import EventsUpdateRequest

from dotenv import load_dotenv

load_dotenv()
parser = argparse.ArgumentParser(description='Update an event in the Fingerprint Server API')
parser.add_argument('--linked_id', type=str)
parser.add_argument('--tag', type=str)
parser.add_argument('--suspect', type=bool)

args = parser.parse_args()
print(f'args: {args.linked_id}, {args.tag}, {args.suspect}')

# configure
configuration = fingerprint_server_sdk.Configuration(
    api_key=os.environ["PRIVATE_KEY"], region=os.environ.get("REGION", "us"))

# create an instance of the API class
api_instance = fingerprint_server_sdk.FingerprintApi(configuration)
request_id = os.environ["REQUEST_ID_TO_UPDATE"]

try:
    updateBody = EventsUpdateRequest(**vars(args))
    print(f'updateBody: {updateBody}')
    api_instance.update_event(updateBody, request_id)
except ApiException as e:
    print("Exception when calling DefaultApi->update_event: %s\n" % e)
    exit(1)

print("Visitor data updated!")

exit(0)
