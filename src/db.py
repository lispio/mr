# -*- coding: utf-8 -*-
import logging
import psycopg2

from src.templates.mrSvrTemplates import db

log = logging.getLogger('mrSvr')


def connect_db():
    conn = psycopg2.connect(database=db.DATABASE.value, user=db.USER.value, host=db.HOST.value, port=db.PORT.value) 
    conn.autocommit = True
    cursor = conn.cursor()
    log.debug(f"Connect to Data base: {db.DATABASE.value}")
    return cursor


def run_query(sql):
    log.debug(f"query: {sql}")
    conn = connect_db()
    conn.execute(sql)
    return conn.fetchall()


def run_update(sql):
    log.debug(f"query: {sql}")
    conn = connect_db()
    conn.execute(sql)
