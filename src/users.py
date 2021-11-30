# -*- coding: utf-8 -*-
import logging
import json

from src.common import convert_to_json
from src.db import run_query, run_update
from src.templates.QueryTemplates import Users
from src.templates.EndpoitnsTemplates import User

from src.ValidateData import validate_user


log = logging.getLogger('mrSvr')


def get_users():
    results = run_query(Users.getUsers.value)
    log.debug(f"Results: {results}")
    return results


def add_user(request):
    run_update(Users.insertUsers.value % (validate_user(convert_to_json(request), User.user_keys.value)[0],
                                          validate_user(convert_to_json(request), User.user_keys.value)[1],
                                          validate_user(convert_to_json(request), User.user_keys.value)[2]))