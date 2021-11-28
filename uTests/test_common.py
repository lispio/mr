from unittest import TestCase
from src.common import get_users


class Test(TestCase):
    def test_get_users(self):
        self.assertIsNotNone(get_users())
