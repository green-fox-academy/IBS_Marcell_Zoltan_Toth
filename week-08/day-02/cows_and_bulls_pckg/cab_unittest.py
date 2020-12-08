import unittest
from cows_and_bulls_pckg.cab import CAB

class TestCAB(unittest.TestCase):

    ex = CAB()

    @classmethod
    def setUp(self):
        self.ex = CAB()
        self.ex.goal = 1234

    '''
    def test_asd(self):
        self.assertEqual(self.ex.guess("asd"), "Incorrect input")
    '''

    def test_0c0b(self):
        self.assertEqual(self.ex.guess("5678"), "0 cows and 0 bulls")

    def test_1c0b(self):
        self.assertEqual(self.ex.guess("1678"), "1 cows and 0 bulls")

    def test_2c0b(self):
        self.assertEqual(self.ex.guess("1278"), "2 cows and 0 bulls")

    def test_3c0b(self):
        self.assertEqual(self.ex.guess("1238"), "3 cows and 0 bulls")

    def test_4c0b(self):
        self.assertEqual(self.ex.guess("1234"), "4 cows and 0 bulls")

    def test_0c1b(self):
        self.assertEqual(self.ex.guess("5671"), "0 cows and 1 bulls")

    def test_0c2b(self):
        self.assertEqual(self.ex.guess("5612"), "0 cows and 2 bulls")

    def test_0c3b(self):
        self.assertEqual(self.ex.guess("5123"), "0 cows and 3 bulls")

    def test_0c4b(self):
        self.assertEqual(self.ex.guess("4321"), "0 cows and 4 bulls")

