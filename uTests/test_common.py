from unittest import TestCase

from src.db import run_query, run_update
from src.common import get_users, add_user

from uTests.TestTemplates import CommonTests as ct


class Test(TestCase):
    def setUp(self):
        pass

    def tearDown(self) -> None:
        run_update(ct.DeleteTestUser.value)

    def test_get_users(self):
        self.assertIsNotNone(get_users())

    def test_add_user(self):
        user_count_before = run_query(ct.CountUsers.value)
        add_user(ct.User.value["name"], ct.User.value["password"], ct.User.value["email"])
        user_count_after = run_query(ct.CountUsers.value)
        self.assertGreater(user_count_after[0], user_count_before[0])
