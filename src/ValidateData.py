import json
import logging

log = logging.getLogger('mrSvr')


def check_keys(request, key):
    try:
        value = request[key]
        return value
    except KeyError:
        log.error(f"key {key} don't exist in {request}")


def validate_user(request, template):
    data = []
    for key in template:
        if check_keys(request, key):
            data.append(request[key])
    return data


def validate_recipes(request):
    print(request)
