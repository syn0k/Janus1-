import unittest
from math import pi
from code_testing import circle_area

class TestCircleArea(unittest.TestCase)

    def test_area(self):
        self.assertEqual(circle_area(3), pi*3**2)
        self.assertEqual(circle_area(1), pi)
        self.assertEqual(circle_area(0), 0)
        self.assertEqual(circle_area(2.5), pi*2.5**2)
