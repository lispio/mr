# -*- coding: utf-8 -*-
from enum import Enum


class db(Enum):
    DATABASE = "mr"
    USER = 'it'
    HOST = '127.0.0.1'
    PORT = '5432'


class MrSvr(Enum):
    port = 8787
