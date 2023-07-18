"""Unit test for rectangle.py"""

import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """Testing rectangle.py"""

    def test_init(self):
        r1 = Rectangle(10, 5)
        self.assertEqual(r1.width, 10)
        self.assertEqual(r1.height, 5)
        self.assertEqual(r1.x, 0)
        self.assertEqual(r1.y, 0)
        self.assertEqual(r1.id, 1)
