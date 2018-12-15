
import unittest
from common import str_tools


class TestStrTools(unittest.TestCase):
    def test_is_chinese(self):
        self.assertEqual(True, str_tools.is_chinese('中'))
        self.assertEqual(False, str_tools.is_chinese('a'))
        self.assertEqual(False, str_tools.is_chinese(''))
        self.assertEqual(False, str_tools.is_chinese('中文'))


if __name__ == '__main__':
    unittest.main()