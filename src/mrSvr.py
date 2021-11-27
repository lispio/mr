#!/opt/lispio/mr/mrSvr_venv/bin/python
# -*- coding: utf-8 -*-

import logging

from twisted.web import resource

log = logging.getLogger()


class Simple(resource.Resource):
    isLeaf = True

    def render_GET(self, request):
        log.info("first endpoint")
        return b"Manny's recipes version 0.0.0-1"
