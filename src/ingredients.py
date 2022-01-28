# -*- coding: utf-8 -*-
import logging
from src.db import run_query, run_update
from src.templates.QueryTemplates import qtIngredients

log = logging.getLogger('mrSvr')


def getIngredients():
    return ingredients_response(run_query(qtIngredients.getIngredients.value))


def addIngredients(naem):
    pass


def ingredients_response(ing_data):
    ing_response = {}
    for i in ing_data:
        ing_response[i[0]] = {'id': i[0], 'name': i[1]}

    return ing_response
