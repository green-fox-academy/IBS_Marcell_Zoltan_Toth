import unittest
from fibonacci_pckg.fibonacci import Fibo

class FiboTest(unittest.TestCase):

    def test_numbers(self):
        f = Fibo()

        self.assertEqual(f.num_fibonacci(1),1)
        self.assertEqual(f.num_fibonacci(2), 1)
        self.assertEqual(f.num_fibonacci(3), 2)
        self.assertEqual(f.num_fibonacci(4), 3)
        self.assertEqual(f.num_fibonacci(5), 5)
        self.assertEqual(f.num_fibonacci(20), 6765)