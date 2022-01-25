#!/opt/lispio/mr/mrSvr_venv/bin/python
# -*- coding: utf-8 -*-
import logging

from fastapi import FastAPI, status, Response

from src.users import getUsers, addUser, deleteUser
from src.userGroup import getGroups
from src.recipes import Recipes

from src.templates.Delete_Templates import DeleteUserOut
from src.templates.GET_templates import UserOut, GroupsOut
from src.templates.POST_templates import RecipesIn, RecipesOut, AddUserIn, AddUserOut, StepsUpdate


log = logging.getLogger('mrSvr')

app = FastAPI()

rec = Recipes()


@app.get("/")
async def root():
    return {"message": "Hello World im Mannis's Recipes"}


@app.get("/recipes")
async def get_recipes(response: Response):
    grec = rec.get_recipes()
    if grec:
        return grec
    else:
        response.status_code = status.HTTP_404_NOT_FOUND


@app.get("/my_recipes")
async def get_recipes_my(username: str, response: Response):
    gMyRec = rec.get_recipes_my(username)
    if gMyRec:
        return gMyRec
    else:
        response.status_code = status.HTTP_404_NOT_FOUND


@app.get("/recipes_user")
async def get_recipes_user(username: str, response: Response):
    grec = rec.get_recipes(username)
    if grec:
        return grec
    else:
        response.status_code = status.HTTP_404_NOT_FOUND


@app.get("/recipes_steps")
async def get_recipesSteps(recipesName: str, response: Response):
    steps = rec.get_steps(recipesName)
    if steps:
        return steps
    else:
        response.status_code = status.HTTP_404_NOT_FOUND


@app.get("/recipes_ming")
async def get_recipesMing(recipesName: str, response: Response):
    ming = rec.get_ming(recipesName)
    if ming:
        return ming
    else:
        response.status_code = status.HTTP_404_NOT_FOUND


@app.get("/get_users/", response_model=UserOut, response_model_exclude_unset=True, status_code=200)
async def get_user_id(username: str, response: Response):
    guser = getUsers(username)
    if guser:
        return guser[username]
    else:
        response.status_code = status.HTTP_404_NOT_FOUND


@app.get("/find_recipes")
async def find_recipes(response: Response):
    response.status_code = status.HTTP_501_NOT_IMPLEMENTED


@app.get("/get_groups/", response_model_exclude_unset=True, status_code=200)
async def get_groups(user_id: int, response: Response):
    groups = getGroups(user_id)
    log.debug(groups)
    if groups:
        return [groups]
    else:
        response.status_code = status.HTTP_404_NOT_FOUND


@app.post("/add_user/", response_model=AddUserOut, response_model_exclude_unset=True, status_code=200)
async def add_users(adduser: AddUserIn, response: Response):
    return addUser(adduser)


@app.post("/add_recipes", response_model=RecipesOut, response_model_exclude_unset=True, status_code=200)
async def add_recipes(recipes: RecipesIn, response: Response):
    results = rec.add_recipes(recipes)
    return results


@app.post("/update_steps", response_model_exclude_unset=True, status_code=200)
async def update_steps(stepUpdate: StepsUpdate):
    rec.update_steps(stepUpdate)


@app.post("/update_recipes")
async def update_recipes(response: Response):
    response.status_code = status.HTTP_501_NOT_IMPLEMENTED


@app.delete("/delete_user/", response_model=DeleteUserOut, response_model_exclude_unset=True, status_code=200)
async def delete_user(userDelete: str, response: Response):
    return deleteUser(userDelete)


@app.delete("/delete_recipe")
async def delete_recipe(recipesName: str):
    return rec.remove_recipes(recipesName)


