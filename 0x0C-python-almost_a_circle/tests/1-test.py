#!/usr/bin/python3
import unittest
from models.base import Base


class TestMaxInteger(unittest.TestCase):
	def oneBase(self):
		self.b1 = Base()
	def TwoBase(self):
		self.b2 = Base()
		self.b2 = Base(0)
	def ThreeBase(self):
		self.b3 = Base(12)

if __name__ == '__main__':
    unittest.main()
