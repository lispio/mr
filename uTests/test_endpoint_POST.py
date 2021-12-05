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

    def test_addUsers(self):
        response = self.client.post("/add_user")
        assert response.status_code == 501

    def test_addRecipes(self):
        response = self.client.post("/add_recipes")
        assert response.status_code == 501

    def test_updateRecipes(self):
        response = self.client.post("/update_recipes")
        assert response.status_code == 501

