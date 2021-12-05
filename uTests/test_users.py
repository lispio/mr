from unittest import TestCase
import json

from src.db import run_query, run_update
from src.users import getUsers, addUser

from uTests.TestTemplates import TUQuery as ct
from src.templates.Templates_POST import AddUser
from uTests.TestTemplates import TUQuery, RecipesTests, TUser


class Test(TestCase):
    def setUp(self):
        run_update(TUQuery.TestUserDB.value)
        self.user_count_before = run_query(ct.CountUsers.value)

    def tearDown(self) -> None:
        run_update(ct.DeleteTestUser.value)

    def test_get_users(self):
        self.assertEquals(len(getUsers(TUser.uName.value)), 1)

