"""Unit test for square.py"""

import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """Testing Base.py"""

    def test_base_init(self):

        b1 = Base()
        self.assertEqual(b1.id, 1)

        b2 = Base(10)
        self.assertEqual(b2.id, 10)
