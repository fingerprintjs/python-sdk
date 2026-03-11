from fingerprint_server_sdk.rest import KnownApiException


def extend_exception(exception, error_object):
    if exception.status == 429:
        try:
            error_object.retry_after = int(exception.headers.get('retry-after'))
        except Exception:
            error_object.retry_after = 1
    return KnownApiException(exception, error_object)
