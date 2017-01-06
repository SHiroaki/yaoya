from unittest import TestCase
from nose.tools import ok_, eq_

def sum(a, b):
    return a + b

class HogeTest(TestCase):
    def test_sum(self):
        eq_(sum(1, 2), 3)
        eq_(sum(3, 4), 7)
        eq_(sum(3, 4), 7)
        eq_(sum(3, 3), 6)
