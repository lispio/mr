# -*- coding: utf-8 -*-
import logging
import json

from src.common import convert_to_json
from src.db import run_query, run_update
from src.templates.QueryTemplates import qtUsers
from src.templates.EndpoitnsTemplates import AddUser

from src.ValidateData import validate_user


log = logging.getLogger('mrSvr')


def get_users():
    results = run_query(qtUsers.getUsers.value)
    log.debug(f"Results: {results}")
    return results


def add_user(request):
    run_update(qtUsers.insertUsers.value % (validate_user(convert_to_json(request), AddUser.user_keys.value)[0],
                                            validate_user(convert_to_json(request), AddUser.user_keys.value)[1],
                                            validate_user(convert_to_json(request), AddUser.user_keys.value)[2]))