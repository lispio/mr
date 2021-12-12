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

    def steps_response(self, steps_data):
        step_response = {}
        for s in steps_data:
            step_response[s[0]] = {'step': s[0], 's_desc': s[1]}

        return step_response

    def get_recipes(self, username=None):
        if username:
            return self.prepare_response(run_query(qtRecipes.getUserRecipes.value % username))

        return self.prepare_response(run_query(qtRecipes.getRecipes.value))

    def add_steps(self, recId, recSteps):
        tmp = ''
        for x in recSteps:
            tmp += f" ({recId[0][0]}, {x.s_num}, '{x.s_desc}'),"
        run_update(qtRecipes.addRecipesSteps.value + tmp[0:-1] + ';')

    def add_ming(self, recId, ming):
        tmp = ''
        for m in ming:
            tmp += f" ({recId[0][0]}, {m.ming_id}, {m.weight}),"

        run_update(qtRecipes.addRecipesMing.value + tmp[0:-1] + ';')

    def add_recipes(self, recipes):
        log.debug(recipes)
        recId = run_query(qtRecipes.addRecipes.value % (recipes.name,
                                                        recipes.user_id,
                                                        recipes.recipes_type,
                                                        recipes.is_public,
                                                        recipes.des))

        if recipes.steps:
            self.add_steps(recId, recipes.steps)

        if recipes.ming:
            self.add_ming(recId, recipes.ming)

        return {"name": f"{recipes.name}", "status": "added"}

    def get_steps(self, recipesName):
        return self.steps_response(run_query(qtRecipes.getRecipesSteps.value % recipesName))

    def get_ming(self, recipesName):
        return run_query(qtRecipes.getRecipesMing.value % recipesName)

    def find_recipes(self):
        pass

    def update_steps(self, stepUpdate):
        print(stepUpdate)

    def remove_recipes(self, recipesName):
        run_update(qtDelete.deleteRecipes.value % recipesName)
        return {"name": recipesName, "status": 'DELETE'}
