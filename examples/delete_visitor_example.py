import os

from dotenv import load_dotenv

import fingerprint_server_sdk
from fingerprint_server_sdk import ApiException
from fingerprint_server_sdk.configuration import Region

load_dotenv()

# configure
region_str = os.environ.get('REGION', 'us').upper()
configuration = fingerprint_server_sdk.Configuration(
    api_key=os.environ['PRIVATE_KEY'], region=Region[region_str]
)

# create an instance of the API class
api_instance = fingerprint_server_sdk.FingerprintApi(configuration)
visitor_id = os.environ['VISITOR_ID_TO_DELETE']

try:
    api_instance.delete_visitor_data(visitor_id)
except ApiException as e:
    print(f'Exception when calling delete_visitor_data: {e}\n')
    exit(1)

print('Visitor data deleted!')

exit(0)
