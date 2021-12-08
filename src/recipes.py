# -*- coding: utf-8 -*-
import logging
from src.db import run_query, run_update
from src.templates.QueryTemplates import qtRecipes, qtDelete

log = logging.getLogger('mrSvr')


class Recipes:

    def prepare_response(self, items):
        response = {}
        for i in items:
            response[i[0]] = {'name': i[1], 'username': i[2], 'recipes_type': i[3]}

        return response

    def get_recipes(self, username=None):
        if username:
            return self.prepare_response(run_query(qtRecipes.getUserRecipes.value % username))

        return self.prepare_response(run_query(qtRecipes.getRecipes.value))

    def add_recipes(self, recipes):
        log.debug(recipes)
        run_update(qtRecipes.addRecipes.value %
                   (recipes.name,
                    recipes.user_id,
                    recipes.recipes_type,
                    recipes.is_public,
                    recipes.des))

        return {"name": f"{recipes.name}", "status": "added"}

    def find_recipes(self):
        pass

    def update_recipes(self):
        pass

    def remove_recipes(self, recipesname):
        run_update(qtDelete.deleteRecipes.value % recipesname)
        return {"name": recipesname, "status": 'DELETE'}
