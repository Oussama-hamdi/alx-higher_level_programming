"""Unit test for  square.py"""

import unittest
from models.square import Square


class Testsquare(unittest.TestCase):
    """Testing square.py"""

    def test_init(self):
        s1 = Square(5)
        self.assertEqual(s1.size, 5)
        self.assertEqual(s1.x, 0)
        self.assertEqual(s1.y, 0)
        self.assertEqual(s1.id, s1.id)
