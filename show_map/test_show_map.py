from unittest import TestCase
from map_display import  show_map

class TestShow_map(TestCase):
    def test_show(self):
        a=show_map((1024,1024))
        a.show()
