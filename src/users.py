# -*- coding: utf-8 -*-
import logging

from src.db import run_query, run_update
from src.templates.QueryTemplates import qtUsers

log = logging.getLogger('mrSvr')


def addUser(item):
    run_update(qtUsers.addUsers.value % (item.name, item.password, item.email))

    return {"name": item.name, "status": "added"}


def getUsers(username):
    results = run_query(qtUsers.getUsers.value % username)
    if len(results) > 0:
        log.debug(f"Results: {results}")
        items = {
            username: {"user_id": results[0][0], "username": f"{results[0][1]}", "email": f'{results[0][3]}'},
        }

        return items