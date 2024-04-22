#!/usr/bin/python3
import unittest
from models.base import Base
import os

class TestBaseClass(unittest.TestCase):
    def testoneBase(self):
        self.b1 = Base()
        self.assertEqual(b1.id, 1)

    def testTwoBase(self):
        self.b2 = Base()
        self.b2 = Base(0)

    def testThreeBase(self):
        self.b3 = Base(12)

if __name__ == '__main__':
    unittest.main()
