import shortuuid


def request_id(request):
    original_request_id = request.headers.get('X-Request-ID', None)
    return original_request_id if original_request_id else "mk-" + shortuuid.uuid()
