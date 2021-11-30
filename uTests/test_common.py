from unittest import TestCase

from src.common import convert_to_json


class Test(TestCase):

    def test_convert_to_json(self):
        self.assertIsInstance(convert_to_json('{"to" :" 1"}'), dict)
