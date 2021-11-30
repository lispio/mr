# -*- coding: utf-8 -*-
import logging
import json

from src.ValidateData import validate_recipes
from src.common import convert_to_json


def add_recipes(request):
    validate_recipes(convert_to_json(request))


def find_recipes():
    pass


def update_recipes():
    pass


def remove_recipes():
    pass
