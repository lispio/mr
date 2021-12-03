# -*- coding: utf-8 -*-
import logging
import json

from src.common import convert_to_json
from src.db import run_query, run_update
from src.templates.QueryTemplates import qtUsers

log = logging.getLogger('mrSvr')


def getUsers():
    results = run_query(qtUsers.getUsers.value)
    log.debug(f"Results: {results}")
    return results


def addUser(item):
    run_update(qtUsers.addUsers.value % (item.name, item.password, item.email))
    return "user added"
