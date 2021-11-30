#!/opt/lispio/mr/mrSvr_venv/bin/python
# -*- coding: utf-8 -*-

import logging

from twisted.web import resource

from src.common import add_user


log = logging.getLogger('mrSvr')


class MrSvrEndpoints(resource.Resource):
    isLeaf = True

    def render_GET(self, request):
        if request.uri == b'/id':
            response = b"0.0.0-1"
            log.debug(f"endpoint: {request.uri} - Response: {response}")
            return response

        if request.uri == b'/add_user':
            if request.content.getvalue():
                add_user(request.content.getvalue())
                response = b'user_added'
                return response
            else:
                log.error("No data in request")
                raise TypeError("No data in request")

        if request.uri == b'/add_recipes':
            return b''

        if request.uri == b'/find_recipes':
            return b''

        if request.uri == b'update_recipes':
            return b''

        if request.uri == b'/test':
            return b''

        else:
            response = b"Manny's recipes version 0.0.0-1"
            log.debug(f"unknown endpoint: {request.uri} - Response: {response}")
            return response
