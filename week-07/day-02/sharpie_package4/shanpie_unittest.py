import unittest
from sharpie import Sharpie
from sharpie_set import SharpieSet

class TestSharpie(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        pass


    def test_stats(self):
        sp = Sharpie("red", 5)

        self.assertEqual(sp.color, "red")
        self.assertEqual(sp.width, 5)
        self.assertEqual(sp.ink_amount, 100)

    def test_use_sharpie(self):
        sp = Sharpie("red", 5)
        sp.use()

        self.assertEqual(sp.ink_amount, 98)

    def test_sharpie_set_stats(self):
        sp = Sharpie("red", 6)
        sps = SharpieSet()

        sps.add(sp)

        self.assertEqual(sps.sharpies[0].color, "red")
        self.assertEqual(sps.sharpies[0].width, 6)
        self.assertEqual(sps.sharpies[0].ink_amount, 100)

        del sps

    def test_sharpie_set_usable(self):

        '''
        sps1 = SharpieSet()
        sps1.add(Sharpie("red", 5))
        sps1.add(Sharpie("blue", 5))
        sps1.add(Sharpie("green", 5, 0))
        '''

        sps = SharpieSet()
        a = Sharpie("red", 5)
        b = Sharpie("blue", 5)
        c = Sharpie("green", 5, 0)

        sps.add(a)
        sps.add(b)
        sps.add(c)


        self.assertEqual(sps.count_usable(), 2)
