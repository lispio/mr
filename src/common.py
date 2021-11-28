# -*- coding: utf-8 -*-
import logging
import json

from src.db import run_query, run_update
from src.templates.dbTemplates import DbInsert, DbGet
from src.templates.EndpoitnsTemplates import User

from src.ValidateData import validate_user


log = logging.getLogger('mrSvr')


def get_users():
    results = run_query(DbGet.GetUsers.value)
    log.debug(f"Results: {results}")
    return results


def add_user(request):
    run_update(DbInsert.insertUsers.value % (validate_user(convert_to_json(request), User.user_keys.value)[0],
                                             validate_user(convert_to_json(request), User.user_keys.value)[1],
                                             validate_user(convert_to_json(request), User.user_keys.value)[2]))


def convert_to_json(request):
    return json.loads(request)
