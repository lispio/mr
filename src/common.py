# -*- coding: utf-8 -*-
import logging

from src.db import run_query, run_update
from src.templates.dbTemplates import DbInsert, DbGet

log = logging.getLogger('mrSvr')


def get_users():
    results = run_query(DbGet.GetUsers.value)
    log.debug(f"Results: {results}")
    return results


def add_user(name, password, email):
    run_update(DbInsert.insertUsers.value % (name, password, email))
