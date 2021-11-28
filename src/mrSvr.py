#!/opt/lispio/mr/mrSvr_venv/bin/python
# -*- coding: utf-8 -*-

import logging

from twisted.web import resource

from src.common import get_users, add_user

log = logging.getLogger('mrSvr')


class MrSvrEndpoints(resource.Resource):
    isLeaf = True

    def render_GET(self, request):
        if request.uri == b'/id':
            response = b"0.0.0-1"
            log.debug(f"endpoint: {request.uri} - Response: {response}")
            add_user('T13', '15', 'jakis@email')
            return response

        if request.uri == b'/add_user':
            response = b'user_added'
            return response

        if request.uri == b'/test':
            temp = request.content.getvalue()
            print(temp)
            return b''

        else:
            response = b"Manny's recipes version 0.0.0-1"
            log.debug(f"unknown endpoint: {request.uri} - Response: {response}")
            return response

