# -*- coding: utf-8 -*-
import logging
import json

from src.ValidateData import validate_recipes
from src.common import convert_to_json


class Recipes:

    def add_recipes(self, request):
        validate_recipes(convert_to_json(request))

    def find_recipes(self):
        pass

    def update_recipes(self):
        pass

    def remove_recipes(self):
        pass
