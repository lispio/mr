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

    def test_deleteUser(self):
        response = self.client.delete("/delete_user")
        assert response.status_code == 501

    def test_deleteRecipe(self):
        response = self.client.delete("/delete_recipe")
        assert response.status_code == 501
