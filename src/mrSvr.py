#!/opt/lispio/mr/mrSvr_venv/bin/python
# -*- coding: utf-8 -*-

import logging

from twisted.web import resource

log = logging.getLogger('mrSvr')


class MrSvrEndpoints(resource.Resource):
    isLeaf = True

    def render_GET(self, request):
        if request.uri == b'/id':
            response = b"0.0.0-1"
            log.debug(f"endpoint: {request.uri} - Response: {response}")
            return response
        else:
            response = b"Manny's recipes version 0.0.0-1"
            log.debug(f"unknown endpoint: {request.uri} - Response: {response}")
            return response

