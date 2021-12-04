from fastapi.testclient import TestClient
from unittest import TestCase
from src.endpoints import app

from src.db import run_query, run_update
from uTests.TestTemplates import TUQuery, RecipesTests


class TestPOST(TestCase):
    def setUp(self):
        self.client = TestClient(app)

    def tearDown(self):
        run_update(TUQuery.DeleteTestUser.value)

    def test_add_users(self):
        response = self.client.post("/add_user", json=TUQuery.User.value)
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