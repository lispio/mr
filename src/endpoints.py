#!/opt/lispio/mr/mrSvr_venv/bin/python
# -*- coding: utf-8 -*-
import json
import logging
from fastapi import FastAPI
from src.users import getUsers
from src.recipes import Recipes
from src.templates.EndpoitnsTemplates import Item, AddUser, AddRecipes
from src.users import addUser
from src.recipes import Recipes


log = logging.getLogger('mrSvr')


app = FastAPI()

rec = Recipes()


@app.get("/")
async def root():
    return {"message": "Hello World im Mannis's Recepis"}


@app.get("/recipes")
async def get_recipes():
    grec = rec.get_recipes()
    if len(grec) > 0:
        return grec
    else:
        return 'Recipes Not Found'


@app.get("/get_users/")
async def get_user_id(uname: str):
    guser = getUsers(uname)
    if len(guser) == 1:
        return getUsers(uname)
    else:
        return 'User Not Found'


@app.get("/find_recipes")
async def find_recipes():
    pass


@app.post("/add_user")
async def add_users(item: AddUser):
    return addUser(item)


@app.post("/add_recipes")
async def add_recipes(item: AddRecipes):
    return "recipes added"


@app.post("/update_recipes")
async def update_recipes():
    pass


@app.delete("/delete_user")
async def delete_user():
    pass


@app.delete("/delete_recipe")
async def delete_recipe():
    pass
