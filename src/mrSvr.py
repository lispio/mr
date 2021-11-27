#!/opt/lispio/mr/mrSvr_venv/bin/python
# -*- coding: utf-8 -*-

from twisted.web import resource


class Simple(resource.Resource):
    isLeaf = True

    def render_GET(self, request):
        return b"Manny's recipes version 0.0.0-1"
