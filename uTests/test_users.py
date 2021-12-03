from unittest import TestCase
import json

from src.db import run_query, run_update
from src.users import getUsers, addUser

from uTests.TestTemplates import UserTests as ct
from src.templates.EndpoitnsTemplates import AddUser


class Test(TestCase):
    def setUp(self):
        self.user_count_before = run_query(ct.CountUsers.value)

    def tearDown(self) -> None:
        run_update(ct.DeleteTestUser.value)

    def test_get_users(self):
        self.assertIsNotNone(getUsers())

