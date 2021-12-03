from fastapi.testclient import TestClient
from unittest import TestCase
from src.endpoints import app

from src.db import run_query, run_update
from uTests.TestTemplates import UserTests, RecipesTests


class TestGET(TestCase):
    def setUp(self):
        run_update(UserTests.TestUserDB.value)
        run_update(RecipesTests.RecipesOne.value)
        self.client = TestClient(app)

    def tearDown(self):
        run_update(UserTests.DeleteTestUser.value)
        run_update(RecipesTests.DeleteRecipes.value)

    def test_root(self):
        response = self.client.get("/")
        assert response.status_code == 200
        assert response.json() == {"message": "Hello World im Mannis's Recepis"}

    def test_get_user_id(self):
        pass

    def test_find_recipes(self):
        response = self.client.get("/recipes")
        assert response.status_code == 200
        assert len(response.json()) == 1


class TestPOST(TestCase):
    def setUp(self):
        self.client = TestClient(app)

    def tearDown(self):
        run_update(UserTests.DeleteTestUser.value)

    def test_add_users(self):
        response = self.client.post("/add_user", json=UserTests.User.value)
        assert response.status_code == 200
        assert response.json() == "user added"

    def test_add_recipes(self):
        pass

    def test_update_recipes(self):
        pass

    def test_delete_user(self):
        pass

    def test_delete_recipe(self):
        pass


