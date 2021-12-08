#!/opt/lispio/mr/mrSvr_venv/bin/python
# -*- coding: utf-8 -*-
import logging

from fastapi import FastAPI, status, Response

from src.users import getUsers, addUser, deleteUser
from src.recipes import Recipes

from src.templates.Delete_Templates import DeleteUserOut
from src.templates.GET_templates import UserOut
from src.templates.POST_templates import RecipesIn, RecipesOut, AddUserIn, AddUserOut


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


@app.get("/recipes_user")
async def get_recipes(username: str, response: Response):
    grec = rec.get_recipes(username)
    if grec:
        return grec
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


@app.post("/add_user/", response_model=AddUserOut, response_model_exclude_unset=True, status_code=200)
async def add_users(adduser: AddUserIn, response: Response):
    return addUser(adduser)


@app.post("/add_recipes", response_model=RecipesOut, response_model_exclude_unset=True, status_code=200)
async def add_recipes(recipes: RecipesIn, response: Response):
    results = rec.add_recipes(recipes)
    return results


@app.post("/update_recipes")
async def update_recipes(response: Response):
    response.status_code = status.HTTP_501_NOT_IMPLEMENTED


@app.delete("/delete_user/", response_model=DeleteUserOut, response_model_exclude_unset=True, status_code=200)
async def delete_user(userDelete: str, response: Response):
    return deleteUser(userDelete)


@app.delete("/delete_recipe")
async def delete_recipe(recepiesname: str):
    return rec.remove_recipes(recepiesname)


