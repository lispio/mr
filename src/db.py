# -*- coding: utf-8 -*-
import os 
import psycopg2
from yoyo import read_migrations, get_backend

from src.templates import db


def connect_db():
    conn = psycopg2.connect(database=db.DATABASE.value, user=db.USER.value, host=db.HOST.value, port=db.PORT.value) 
    conn.autocommit = True
    cursor = conn.cursor()
    return cursor
    
def run_query(sql):
    conn = connect_db()
    conn.execute(sql)
    return conn.fetchall()

def run_update(sql):
    conn = connect_db()
    conn.execute(sql)