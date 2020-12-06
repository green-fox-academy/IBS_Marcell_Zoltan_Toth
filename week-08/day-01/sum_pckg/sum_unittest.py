import unittest
from sum_pckg.sum import Sum


class Sum_test(unittest.TestCase):

    def test_sum_normal(self):
        ex = Sum()

        self.assertEqual(ex.sum([1,2,3]), 6)

    def test_sum_empty(self):
        ex = Sum()

        self.assertEqual(ex.sum([]), 0)

    def test_sum_one(self):
        ex = Sum()

        self.assertEqual(ex.sum([1]), 1)

    def test_sum_none(self):
        ex = Sum()

        self.assertEqual(ex.sum(None), 0)




