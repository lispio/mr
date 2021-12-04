# -*- coding: utf-8 -*-
import logging

from src.db import run_query, run_update
from src.templates.QueryTemplates import qtUsers

log = logging.getLogger('mrSvr')


def addUser(item):
    run_update(qtUsers.addUsers.value % (item.name, item.password, item.email))
    return "user added"


def getUsers(uname):
    results = run_query(qtUsers.getUsers.value % uname)
    log.debug(f"Results: {results}")
    return results
