#!/usr/bin/python3
import unittest
from models.base import Base
import os
from models.rectangle import Rectangle


class TestRectangleClass(unittest.TestCase):
    def testoneRect(self):
        self.b1 = Rectangle(1, 1)
        self.assertEqual(b1.id, 1)

    def testTwoBase(self):
        self.b2 = Rectangle(2, 10)
        self.b2 = Rectangle(0, 2)
        self.assertEqual(b2.id, 2)

    def testThreeBase(self):
        self.b3 = Rectangle(1, 2 , 0, 0, 12)
        self.assertEqual(b3.id, 12)

if __name__ == '__main__':
    unittest.main()
