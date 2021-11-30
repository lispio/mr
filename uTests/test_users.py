from unittest import TestCase

from src.db import run_query, run_update
from src.users import get_users, add_user

from uTests.TestTemplates import CommonTests as ct


class Test(TestCase):
    def setUp(self):
        self.user_count_before = run_query(ct.CountUsers.value)
        add_user(ct.AddUserRequest.value)

    def tearDown(self) -> None:
        run_update(ct.DeleteTestUser.value)

    def test_get_users(self):
        self.assertIsNotNone(get_users())

    def test_add_user(self):
        self.assertGreater(run_query(ct.CountUsers.value)[0][0], self.user_count_before[0][0])

    def test_check_user_in_db(self):
        self.assertEquals(run_query(ct.CountUserName.value)[0][0], 1)
