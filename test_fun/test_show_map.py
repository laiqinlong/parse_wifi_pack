from unittest import TestCase
from map_display import show_map

class TestShow_map(TestCase):
    def test_show_red(self):
        a=show_map()
        a.show_red()
        self.fail()
