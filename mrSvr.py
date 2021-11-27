#!/opt/lispio/fgr/mrSvr_venv/bin/python
# -*- coding: utf-8 -*-

from flask import Flask

mrSvr = Flask(__name__)


@mrSvr.route("/")
def hello_world():
    return "<p>Hello, World!!!!</p>"
