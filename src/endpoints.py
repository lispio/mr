#!/opt/lispio/mr/mrSvr_venv/bin/python
# -*- coding: utf-8 -*-
import json
import logging
from fastapi import FastAPI, status, Response

from src.users import getUsers
from src.templates.Templates_GET import UserOut, UserIn
from src.templates.Templates_POST import AddUser, AddRecipes
from src.users import addUser
from src.recipes import Recipes


log = logging.getLogger('mrSvr')


app = FastAPI()

rec = Recipes()


@app.get("/")
async def root():
    return {"message": "Hello World im Mannis's Recepis"}


@app.get("/recipes")
async def get_recipes(response: Response):
    grec = rec.get_recipes()
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


@app.post("/add_user")
async def add_users(response: Response):
    response.status_code = status.HTTP_501_NOT_IMPLEMENTED


@app.post("/add_recipes")
async def add_recipes(response: Response):
    response.status_code = status.HTTP_501_NOT_IMPLEMENTED


@app.post("/update_recipes")
async def update_recipes(response: Response):
    response.status_code = status.HTTP_501_NOT_IMPLEMENTED


@app.delete("/delete_user")
async def delete_user(response: Response):
    response.status_code = status.HTTP_501_NOT_IMPLEMENTED


@app.delete("/delete_recipe")
async def delete_recipe(response: Response):
    response.status_code = status.HTTP_501_NOT_IMPLEMENTED
