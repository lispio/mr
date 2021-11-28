# -*- coding: utf-8 -*-
from src.db import run_query


def get_users():
    sql = 'SELECT * FROM users'
    results = run_query(sql)
    return results
