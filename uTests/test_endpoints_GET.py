from fastapi.testclient import TestClient
from unittest import TestCase
from src.endpoints import app

from src.db import run_query, run_update
from uTests.TestTemplates import TUQuery, RecipesTests, ResponseGet, TUser


class TestGET(TestCase):
    def setUp(self):
        run_update(TUQuery.TestUserDB.value)
        run_update(RecipesTests.RecipesOne.value)
        self.client = TestClient(app)

    def tearDown(self):
        run_update(TUQuery.DeleteTestUser.value)
        run_update(RecipesTests.DeleteRecipes.value)

    def test_root(self):
        response = self.client.get("/")
        assert response.status_code == 200
        assert response.json() == {"message": "Hello World im Mannis's Recepis"}

    def test_getUserExist(self):
        response = self.client.get("/get_users/?username=%s" % TUser.uName.value)
        assert response.status_code == 200
        assert response.json() == ResponseGet.UserExist.value

    def test_getUserNotExist(self):
        response = self.client.get("/get_users/?username=TetUs")
        assert response.status_code == 404
        assert response.json() is None

    def test_getRecipesExist(self):
        response = self.client.get("/recipes")
        assert response.status_code == 200
        assert response.json() == ResponseGet.RecipesExist.value

    def test_getRecipesNotExist(self):
        run_update(RecipesTests.DeleteRecipes.value)
        response = self.client.get("/recipes")
        assert response.status_code == 404
        assert response.json() is None
