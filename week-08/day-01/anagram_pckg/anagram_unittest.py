import unittest
from anagram_pckg.anagram import Anagram


class TestAnagram(unittest.TestCase):

    def test_anagrams(self):
        angrm = Anagram()
        self.assertEqual(Anagram.is_anagram(Anagram(), "holla", "olhal",), True)
        #calling a static method takes another input, an instance of the method. !!! 
        self.assertTrue(angrm.is_anagram("baby yoda", "dabb aoyy"))

    def test_not_anagrams(self):
        angrm = Anagram()
        self.assertEqual(angrm.is_anagram("farox", "faxol"), False)
        self.assertFalse(angrm.is_anagram("della", "suska"))


if __name__ == '__main__':
    unittest.main()