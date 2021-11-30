# -*- coding: utf-8 -*-
import logging
import json


def convert_to_json(request):
    return json.loads(request)
