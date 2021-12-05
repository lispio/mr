# -*- coding: utf-8 -*-
import logging
from src.db import run_query, run_update
from src.templates.QueryTemplates import qtRecipes
from fastapi import FastAPI, status, Response

log = logging.getLogger('mrSvr')


class Recipes:

    def get_recipes(self, username=None):
        if username:
            return run_query(qtRecipes.getUserRecipes.value % username)

        return run_query(qtRecipes.getRecipes.value)

    def add_recipes(self, recipes):
        log.debug(recipes)
        run_update(qtRecipes.addRecipes.value %
                   (recipes.name,
                    recipes.user_id,
                    recipes.recipes_type,
                    recipes.is_public,
                    recipes.des))
        return 'recipes added'

    def find_recipes(self):
        pass

    def update_recipes(self):
        pass

    def remove_recipes(self):
        pass
