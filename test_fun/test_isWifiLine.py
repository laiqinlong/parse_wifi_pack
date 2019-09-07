from unittest import TestCase
from parse_pack import isWifiLine

class TestIsWifiLine(TestCase):
    def test_isWifiLine(self):
        line=""
        result=isWifiLine(line)
        True_result=False
        self.assertEqual(result,True_result)
