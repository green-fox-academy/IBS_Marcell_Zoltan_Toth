import unittest
from count_letters_pckg.count import Count

class CountTest(unittest.TestCase):

    def test_okay(self):
        ct = Count()
        self.assertEqual(ct.count_letters("letter"), {'l':1, 'e':2, 't':2, 'r':1 })
        self.assertEqual(ct.count_letters("letter"), {'r': 1, 'e': 2, 't': 2, 'l': 1})

