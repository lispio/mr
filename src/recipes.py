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

    def add_steps(self, recId, recSteps):
        tmp = ''
        for x in recSteps.steps:
            tmp += f" ({recId}, {x.s_number}, '{x.s_desc}'),"
        run_update(qtRecipes.addRecipesSteps.value + tmp[0:-1] + ';')

    def add_recipes(self, recipes):
        log.debug(recipes)
        recId = run_query(qtRecipes.addRecipes.value % (recipes.name,
                                                        recipes.user_id,
                                                        recipes.recipes_type,
                                                        recipes.is_public,
                                                        recipes.des))

        if recipes.steps:
            self.add_steps(recId, recipes.steps)

        return {"name": f"{recipes.name}", "status": "added"}

    def find_recipes(self):
        pass

    def update_recipes(self):
        pass

    def remove_recipes(self, recipesName):
        run_update(qtDelete.deleteRecipes.value % recipesName)
        return {"name": recipesName, "status": 'DELETE'}
