from unittest import TestCase
from parse_map_data import new_whole_map

class TestNew_whole_map(TestCase):
    def test_new_whole_map(self):
        test_case = [0x0, 0x0, 0x0, 0x43, 0x1f, 0x0, 0x44, 0x51, 0x8, 0x6, 0x47, 0x82, 0x46, 0xe1, 0x43, 0x3]
        test_case = str(test_case)
        test_line = test_case.replace(',',' ')
        print(test_line)
        result = new_whole_map(test_line)
        true_result = ''
        self.assertEqual(true_result,result)
