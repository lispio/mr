# -*- coding: utf-8 -*-
import logging
from src.db import run_query
from src.templates.QueryTemplates import qtRecipes

log = logging.getLogger('mrSvr')


class Recipes:

    def get_recipes(self, username=None):
        if username:
            return run_query(qtRecipes.getUserRecipes.value % username)

        return run_query(qtRecipes.getRecipes.value)

    def add_recipes(self, recipes):
        log.debug(recipes)

    def find_recipes(self):
        pass

    def update_recipes(self):
        pass

    def remove_recipes(self):
        pass
