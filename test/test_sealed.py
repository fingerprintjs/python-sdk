import base64
import io
import json
import unittest
from unittest import expectedFailure

from fingerprint_server_sdk import ApiClientDeserializer, DecryptionAlgorithm, DecryptionKey, \
    unseal_event_response, UnsealError, UnsealAggregateError, EventsGetResponse, Products, \
    ProductIdentification, BrowserDetails

class TestSealed(unittest.TestCase):
    valid_key = base64.b64decode('p2PA7MGy5tx56cnyJaFZMr96BCFwZeHjZV2EqMvTq53=')
    invalid_key = base64.b64decode('a2PA7MGy5tx56cnyJaFZMr96BCFwZeHjZV2EqMvTq53=')

    def test_unseal_aes256gcm(self):
        sealed_result = '''{
  "products": {
    "identification": {
      "data": {
        "visitorId": "2ZEDCZEfOfXjEmMuE3tq",
        "requestId": "1703067132750.Z5hutJ",
        "browserDetails": {
          "browserName": "Safari",
          "browserMajorVersion": "17",
          "browserFullVersion": "17.3",
          "os": "Mac OS X",
          "osVersion": "10.15.7",
          "device": "Other",
          "userAgent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.3 Safari/605.1.15"
        },
        "incognito": false,
        "ip": "::1",
        "ipLocation": {
          "accuracyRadius": 1000,
          "latitude": 59.3241,
          "longitude": 18.0517,
          "postalCode": "100 05",
          "timezone": "Europe/Stockholm",
          "city": {
            "name": "Stockholm"
          },
          "country": {
            "code": "SE",
            "name": "Sweden"
          },
          "continent": {
            "code": "EU",
            "name": "Europe"
          },
          "subdivisions": [
            {
              "isoCode": "AB",
              "name": "Stockholm County"
            }
          ]
        },
        "timestamp": 1703067136286,
        "time": "2023-12-20T10:12:16Z",
        "url": "http://localhost:8080/",
        "tag": {
          "foo": "bar"
        },
        "confidence": {
          "score": 1
        },
        "visitorFound": true,
        "firstSeenAt": {
          "global": "2023-12-15T12:13:55.103Z",
          "subscription": "2023-12-15T12:13:55.103Z"
        },
        "lastSeenAt": {
          "global": "2023-12-19T11:39:51.52Z",
          "subscription": "2023-12-19T11:39:51.52Z"
        },
        "replayed": false
      }
    },
    "botd": {
      "data": {
        "bot": {
          "result": "notDetected"
        },
        "meta": {
          "foo": "bar"
        },
        "url": "http://localhost:8080/",
        "ip": "::1",
        "time": "2023-12-20T10:12:13.894Z",
        "userAgent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.3 Safari/605.1.15",
        "requestId": "1703067132750.Z5hutJ"
      }
    }
  }
}'''
        expected_result = ApiClientDeserializer.deserialize(json.loads(sealed_result), 'EventsGetResponse')

        sealed_data = base64.b64decode(
            'noXc7etL3WJZn6BSZLV4tcjBr0uFr4+qvDrSdcZ9M1bb1MB+/le7UKY+6FJNFQHBm64X1/GVE3xkjBuW4mveH3jEK8cOSWBhl71tgYegxm+MkRHRAYM7vDPOS4sw1rb6xqdVZ/sovFP6yIqNRhrKWdO/B99vtext6l/NWlmXfTCoX3LHXYK94yr0O4eptZBwBK70fMB0YBR6iw1/zJOs9W6LZ50d2ml4wl/Ah1qJKmQueraKJaIIAQEUNbOm8ReoRsDrAWsVbIv2IscKEGNwZEjd5V1nZFkHLzOUQGKLjFQqGxFFmxV/PuDZve/lHyjmn9q3+UFJzJKXVOLyPTjhwQdjouvdJn5k9FEpH0hua+/KgSrcIKnKXtk7zPXAFEo9FeQJA3XJH8+dHcDgadl6/FIrAxtqrMRbngp7wKpltIySaCMi9P0qYoWnVvQC3gyc5xoW00UxcdPfXnQR9F21QfZ3EzULIbJQ5sUjwcg31h/IszlBXueHnGEiszhdXAIOHU865FLJsvLAqZD1A+R9/gurAG3kck1A/t8Vf8znmd8WeMezj0KObenNhHeDpjAFcAZS6evr8gDb/IZ6Ge3CUzBvfXUZNNlhEujS6yo/eK/plFACtbbIMiosQq1zRIMlLmAvlb42jNAwPtjb2JQhO+AP+EUUEe8nTDjyytZIHThzuipfVIRpxEbV9MdYt0Ri5EqI4LA2YiAMmphdaio4grw51oD63GgSeKXEUi1YoLUGmXCNbn5Q1vcQiGd5O+TJ3WzacMcBcPDFd9ZxVxe8qmn3gXWXlod4NmS5nhksiiYY0UUWqMMqEEZou5LhwV8FrQdebBNDQ9GKoGkaadJoJzkKZWYlO0ju5EYTlQCUTvHenefVmrHUccteVuwz6Fsp3d5p3SBGumpbdECjUMnO2OWkOzf4S0TArorl8KnB3TidzsM94eTr0M+/uz910HmnOqIYms80IBV3yFS0CEvcvuyjnEpW/vfOIbs0qFycNx34Hltqa0PdSSzcrFfMJjR5h9g/hORaO4MNXu9ORw==')

        result = unseal_event_response(sealed_data, [
            DecryptionKey(self.invalid_key, DecryptionAlgorithm['Aes256Gcm']),
            DecryptionKey(self.valid_key, DecryptionAlgorithm['Aes256Gcm']),
        ])

        self.assertEqual(result, expected_result)
        self.assertIsInstance(result, EventsGetResponse)
        self.assertIsInstance(result.products, Products)
        self.assertIsInstance(result.products.identification, ProductIdentification)
        self.assertIsInstance(result.products.identification.data.browser_details, BrowserDetails)


    def test_unseal_invalid_header(self):
        sealed_data = base64.b64decode(
            'xzXc7SXO+mqeAGrvBMgObi/S0fXTpP3zupk8qFqsO/1zdtWCD169iLA3VkkZh9ICHpZ0oWRzqG0M9/TnCeKFohgBLqDp6O0zEfXOv6i5q++aucItznQdLwrKLP+O0blfb4dWVI8/aSbd4ELAZuJJxj9bCoVZ1vk+ShbUXCRZTD30OIEAr3eiG9aw00y1UZIqMgX6CkFlU9L9OnKLsNsyomPIaRHTmgVTI5kNhrnVNyNsnzt9rY7fUD52DQxJILVPrUJ1Q+qW7VyNslzGYBPG0DyYlKbRAomKJDQIkdj/Uwa6bhSTq4XYNVvbk5AJ/dGwvsVdOnkMT2Ipd67KwbKfw5bqQj/cw6bj8Cp2FD4Dy4Ud4daBpPRsCyxBM2jOjVz1B/lAyrOp8BweXOXYugwdPyEn38MBZ5oL4D38jIwR/QiVnMHpERh93jtgwh9Abza6i4/zZaDAbPhtZLXSM5ztdctv8bAb63CppLU541Kf4OaLO3QLvfLRXK2n8bwEwzVAqQ22dyzt6/vPiRbZ5akh8JB6QFXG0QJF9DejsIspKF3JvOKjG2edmC9o+GfL3hwDBiihYXCGY9lElZICAdt+7rZm5UxMx7STrVKy81xcvfaIp1BwGh/HyMsJnkE8IczzRFpLlHGYuNDxdLoBjiifrmHvOCUDcV8UvhSV+UAZtAVejdNGo5G/bz0NF21HUO4pVRPu6RqZIs/aX4hlm6iO/0Ru00ct8pfadUIgRcephTuFC2fHyZxNBC6NApRtLSNLfzYTTo/uSjgcu6rLWiNo5G7yfrM45RXjalFEFzk75Z/fu9lCJJa5uLFgDNKlU+IaFjArfXJCll3apbZp4/LNKiU35ZlB7ZmjDTrji1wLep8iRVVEGht/DW00MTok7Zn7Fv+MlxgWmbZB3BuezwTmXb/fNw==')

        with self.assertRaisesRegex(ValueError, "Invalid sealed data header"):
            unseal_event_response(sealed_data, [
                DecryptionKey(self.invalid_key, DecryptionAlgorithm['Aes256Gcm']),
                DecryptionKey(self.valid_key, DecryptionAlgorithm['Aes256Gcm']),
            ])

    def test_unseal_invalid_algorithm(self):
        sealed_data = base64.b64decode(
            'noXc7SXO+mqeAGrvBMgObi/S0fXTpP3zupk8qFqsO/1zdtWCD169iLA3VkkZh9ICHpZ0oWRzqG0M9/TnCeKFohgBLqDp6O0zEfXOv6i5q++aucItznQdLwrKLP+O0blfb4dWVI8/aSbd4ELAZuJJxj9bCoVZ1vk+ShbUXCRZTD30OIEAr3eiG9aw00y1UZIqMgX6CkFlU9L9OnKLsNsyomPIaRHTmgVTI5kNhrnVNyNsnzt9rY7fUD52DQxJILVPrUJ1Q+qW7VyNslzGYBPG0DyYlKbRAomKJDQIkdj/Uwa6bhSTq4XYNVvbk5AJ/dGwvsVdOnkMT2Ipd67KwbKfw5bqQj/cw6bj8Cp2FD4Dy4Ud4daBpPRsCyxBM2jOjVz1B/lAyrOp8BweXOXYugwdPyEn38MBZ5oL4D38jIwR/QiVnMHpERh93jtgwh9Abza6i4/zZaDAbPhtZLXSM5ztdctv8bAb63CppLU541Kf4OaLO3QLvfLRXK2n8bwEwzVAqQ22dyzt6/vPiRbZ5akh8JB6QFXG0QJF9DejsIspKF3JvOKjG2edmC9o+GfL3hwDBiihYXCGY9lElZICAdt+7rZm5UxMx7STrVKy81xcvfaIp1BwGh/HyMsJnkE8IczzRFpLlHGYuNDxdLoBjiifrmHvOCUDcV8UvhSV+UAZtAVejdNGo5G/bz0NF21HUO4pVRPu6RqZIs/aX4hlm6iO/0Ru00ct8pfadUIgRcephTuFC2fHyZxNBC6NApRtLSNLfzYTTo/uSjgcu6rLWiNo5G7yfrM45RXjalFEFzk75Z/fu9lCJJa5uLFgDNKlU+IaFjArfXJCll3apbZp4/LNKiU35ZlB7ZmjDTrji1wLep8iRVVEGht/DW00MTok7Zn7Fv+MlxgWmbZB3BuezwTmXb/fNw==')

        with self.assertRaisesRegex(ValueError, "Unsupported decryption algorithm: invalid"):
            unseal_event_response(sealed_data, [
                DecryptionKey(self.invalid_key, 'invalid'),
                DecryptionKey(self.valid_key, DecryptionAlgorithm['Aes256Gcm']),
            ])

    def test_unseal_invalid_data(self):
        sealed_data = base64.b64decode(
            # "{\"invalid\":true}"
            'noXc7VOpBstjjcavDKSKr4HTavt4mdq8h6NC32T0hUtw9S0jXT8lPjZiWL8SyHxmrF3uTGqO+g==')

        with self.assertRaisesRegex(ValueError, "Sealed data is not valid event response"):
            unseal_event_response(sealed_data, [
                DecryptionKey(self.invalid_key, DecryptionAlgorithm['Aes256Gcm']),
                DecryptionKey(self.valid_key, DecryptionAlgorithm['Aes256Gcm']),
            ])

    def test_unseal_not_compressed_data(self):
        sealed_data = base64.b64decode(
            'noXc7dtuk0smGE+ZbaoXzrp6Rq8ySxLepejTsu7+jUXlPhV1w+WuHx9gbPhaENJnOQo8BcGmsaRhL5k2NVj+DRNzYO9cQD7wHxmXKCyTbl/dvSYOMoHziUZ2VbQ7tmaorFny26v8jROr/UBGfvPE0dLKC36IN9ZlJ3X0NZJO8SY+8bCr4mTrkVZsv/hpvZp+OjC4h7e5vxcpmnBWXzxfaO79Lq3aMRIEf9XfK7/bVIptHaEqtPKCTwl9rz1KUpUUNQSHTPM0NlqJe9bjYf5mr1uYvWHhcJoXSyRyVMxIv/quRiw3SKJzAMOTBiAvFICpWuRFa+T/xIMHK0g96w/IMQo0jdY1E067ZEvBUOBmsJnGJg1LllS3rbJVe+E2ClFNL8SzFphyvtlcfvYB+SVSD4bzI0w/YCldv5Sq42BFt5bn4n4aE5A6658DYsfSRYWqP6OpqPJx96cY34W7H1t/ZG0ulez6zF5NvWhc1HDQ1gMtXd+K/ogt1n+FyFtn8xzvtSGkmrc2jJgYNI5Pd0Z0ent73z0MKbJx9v2ta/emPEzPr3cndN5amdr6TmRkDU4bq0vyhAh87DJrAnJQLdrvYLddnrr8xTdeXxj1i1Yug6SGncPh9sbTYkdOfuamPAYOuiJVBAMcfYsYEiQndZe8mOQ4bpCr+hxAAqixhZ16pQ8CeUwa247+D2scRymLB8qJXlaERuFZtWGVAZ8VP/GS/9EXjrzpjGX9vlrIPeJP8fh2S5QPzw55cGNJ7JfAdOyManXnoEw2/QzDhSZQARVl+akFgSO0Y13YmbiL7H6HcKWGcJ2ipDKIaj2fJ7GE0Vzyt+CBEezSQR99Igd8x3p2JtvsVKp35iLPksjS1VqtSCTbuIRUlINlfQHNjeQiE/B/61jo3Mf7SmjYjqtvXt5e9RKb+CQku2qH4ZU8xN3DSg+4mLom3BgKBkm/MoyGBpMK41c96d2tRp3tp4hV0F6ac02Crg7P2lw8IUct+i2VJ8VUjcbRfTIPQs0HjNjM6/gLfLCkWOHYrlFjwusXWQCJz91Kq+hVxj7M9LtplPO4AUq6RUMNhlPGUmyOI2tcUMrjq9vMLXGlfdkH185zM4Mk+O7DRLC8683lXZFZvcBEmxr855PqLLH/9SpYKHBoGRatDRdQe3oRp6gHS0jpQ1SW/si4kvLKiUNjiBExvbQVOUV7/VFXvG1RpM9wbzSoOd40gg7ZzD/72QshUC/25DkM/Pm7RBzwtjgmnRKjT+mROeC/7VQLoz3amv09O8Mvbt+h/lX5+51Q834F7NgIGagbB20WtWcMtrmKrvCEZlaoiZrmYVSbi1RfknRK7CTPJkopw9IjO7Ut2EhKZ+jL4rwk6TlVm6EC6Kuj7KNqp6wB/UNe9eM2Eym/aiHAcja8XN4YQhSIuJD2Wxb0n3LkKnAjK1/GY65c8K6rZsVYQ0MQL1j4lMl0UZPjG/vzKyetIsVDyXc4J9ZhOEMYnt/LaxEeSt4EMJGBA9wpTmz33X4h3ij0Y3DY/rH7lrEScUknw20swTZRm5T6q1bnimj7M1OiOkebdI09MZ0nyaTWRHdB7B52C/moh89Q7qa2Fulp5h8Us1FYRkWBLt37a5rGI1IfVeP38KaPbagND+XzWpNqX4HVrAVPLQVK5EwUvGamED3ooJ0FMieTc0IH0N+IeUYG7Q8XmrRVBcw32W8pEfYLO9L71An/J0jQZCIP8DuQnUG0mOvunOuloBGvP/9LvkBlkamh68F0a5f5ny1jloyIFJhRh5dt2SBlbsXS9AKqUwARYSSsA9Ao4WJWOZMyjp8A+qIBAfW65MdhhUDKYMBgIAbMCc3uiptzElQQopE5TT5xIhwfYxa503jVzQbz1Q==')

        with self.assertRaisesRegex(UnsealAggregateError, "Unable to decrypt sealed data") as context:
            unseal_event_response(sealed_data, [
                DecryptionKey(self.invalid_key, DecryptionAlgorithm['Aes256Gcm']),
                DecryptionKey(self.valid_key, DecryptionAlgorithm['Aes256Gcm']),
            ])

        exception: UnsealAggregateError = context.exception
        error: UnsealError = exception.errors[1]

        self.assertEqual(str(error.exception), 'Error -3 while decompressing data: invalid distance too far back')

    def test_unseal_all_keys_invalid(self):
        sealed_data = base64.b64decode(
            'noXc7SXO+mqeAGrvBMgObi/S0fXTpP3zupk8qFqsO/1zdtWCD169iLA3VkkZh9ICHpZ0oWRzqG0M9/TnCeKFohgBLqDp6O0zEfXOv6i5q++aucItznQdLwrKLP+O0blfb4dWVI8/aSbd4ELAZuJJxj9bCoVZ1vk+ShbUXCRZTD30OIEAr3eiG9aw00y1UZIqMgX6CkFlU9L9OnKLsNsyomPIaRHTmgVTI5kNhrnVNyNsnzt9rY7fUD52DQxJILVPrUJ1Q+qW7VyNslzGYBPG0DyYlKbRAomKJDQIkdj/Uwa6bhSTq4XYNVvbk5AJ/dGwvsVdOnkMT2Ipd67KwbKfw5bqQj/cw6bj8Cp2FD4Dy4Ud4daBpPRsCyxBM2jOjVz1B/lAyrOp8BweXOXYugwdPyEn38MBZ5oL4D38jIwR/QiVnMHpERh93jtgwh9Abza6i4/zZaDAbPhtZLXSM5ztdctv8bAb63CppLU541Kf4OaLO3QLvfLRXK2n8bwEwzVAqQ22dyzt6/vPiRbZ5akh8JB6QFXG0QJF9DejsIspKF3JvOKjG2edmC9o+GfL3hwDBiihYXCGY9lElZICAdt+7rZm5UxMx7STrVKy81xcvfaIp1BwGh/HyMsJnkE8IczzRFpLlHGYuNDxdLoBjiifrmHvOCUDcV8UvhSV+UAZtAVejdNGo5G/bz0NF21HUO4pVRPu6RqZIs/aX4hlm6iO/0Ru00ct8pfadUIgRcephTuFC2fHyZxNBC6NApRtLSNLfzYTTo/uSjgcu6rLWiNo5G7yfrM45RXjalFEFzk75Z/fu9lCJJa5uLFgDNKlU+IaFjArfXJCll3apbZp4/LNKiU35ZlB7ZmjDTrji1wLep8iRVVEGht/DW00MTok7Zn7Fv+MlxgWmbZB3BuezwTmXb/fNw==')

        with self.assertRaisesRegex(UnsealAggregateError, 'Unable to decrypt sealed data'):
            unseal_event_response(sealed_data, [
                DecryptionKey(self.invalid_key, DecryptionAlgorithm['Aes256Gcm']),
                DecryptionKey(self.invalid_key, DecryptionAlgorithm['Aes256Gcm']),
            ])

    def test_unseal_empty_data(self):
        sealed_data = bytearray(b'')

        with self.assertRaisesRegex(ValueError, 'Invalid sealed data header'):
            unseal_event_response(sealed_data, [
                DecryptionKey(self.invalid_key, DecryptionAlgorithm['Aes256Gcm']),
                DecryptionKey(self.valid_key, DecryptionAlgorithm['Aes256Gcm']),
            ])

    def test_unseal_invalid_nonce(self):
        sealed_data = bytes([0x9E, 0x85, 0xDC, 0xED, 0xAA, 0xBB, 0xCC])

        with self.assertRaisesRegex(UnsealAggregateError, 'Unable to decrypt sealed data') as context:
            unseal_event_response(sealed_data, [
                DecryptionKey(self.invalid_key, DecryptionAlgorithm['Aes256Gcm']),
                DecryptionKey(self.valid_key, DecryptionAlgorithm['Aes256Gcm']),
            ])

        exception: UnsealAggregateError = context.exception
        error: UnsealError = exception.errors[1]

        self.assertEqual(str(error.exception), 'initialization_vector must be between 8 and 128 bytes (64 and 1024 bits).')


