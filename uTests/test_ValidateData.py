from unittest import TestCase

from src.ValidateData import check_keys, validate_user

from uTests.TestTemplates import ValidateDataTests as vdt


class Test(TestCase):
    def test_check_keys(self):
        self.assertEquals(check_keys(vdt.TestDict.value, "Test1"), "test1")

    def test_check_keys_not_exist(self):
        self.assertIsNone(check_keys(vdt.TestDict.value, 'test'))

    def test_validate_user(self):
        self.assertEquals(validate_user(vdt.TestAddUserRequest.value, vdt.TestUserKeys.value), vdt.TestUserData.value)

