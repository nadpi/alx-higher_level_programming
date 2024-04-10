#!/usr/bin/python3
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):

    def testIfOneNum(self):
        self.num = max_integer([1])

    def testIfNoNum(self):
        self.num = max_integer([])

    def testRight(self):
        self.num1 = max_integer([1, 2, 3, 4])
        self.num2 = max_integer([1, 3, 4, 2])

if __name__ == '__main__':
    unittest.main()
