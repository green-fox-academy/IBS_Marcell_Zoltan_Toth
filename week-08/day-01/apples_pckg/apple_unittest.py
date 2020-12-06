import unittest
from apples_pckg.apple import Apple

class Apple_test(unittest.TestCase):

    def test_value(self):
        apple = Apple()

        self.assertEqual(apple.get_apple(), "apple")




if __name__ == '__main__':
    unittest.main()