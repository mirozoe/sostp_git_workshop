import unittest
from random import randint

def generate_num():
    return randint(10, 20)

class basicTest(unittest.TestCase):
    def test(self):
        self.assertGreater(generate_num(), 9)
        self.assertLess(generate_num(),21)
