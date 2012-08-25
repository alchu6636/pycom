from pcclass import PcInt, PcFloat
import unittest

class TestPcInt(unittest.TestCase):

    def setUp(self):
        self.i3 = PcInt(3)
        self.i2 = PcInt(2)
        self.f025 = PcFloat(0.25)

    def test_init(self):
        PcInt(3)

    def test_add_int(self):
        result = self.i3._add_int(self.i2)
        self.assertEqual(result, PcInt(5))

    def test_add_float(self):
        result = self.i3._add_float(self.f025)
        self.assertEqual(result, PcFloat(3.25))

    def test_add(self):
        self.assertEqual(self.i3.add(self.i2), PcInt(5))
        self.assertEqual(self.i3.add(self.f025), PcFloat(3.25))

class TestPcFloat(unittest.TestCase):

    def test_add(self):
        a = PcFloat(0.125)
        b = PcFloat(0.25)
        c = a.add(b)
        self.assertEqual(c, PcFloat(0.375))

    def test_add_float(self):
        a = PcFloat(3.0)
        b = PcFloat(0.125)
        self.assertEqual(a._add_float(b), PcFloat(3.125))

    def test_add_int(self):
        a = PcFloat(3.25)
        b = PcInt(1)
        self.assertEqual(a._add_int(b), PcFloat(4.25))

    def test_add(self):
        f35 = PcFloat(3.5)
        f025 = PcFloat(0.25) 
        i2 = PcInt(2)
        self.assertEqual(f35.add(f025), PcFloat(3.75))
        self.assertEqual(f35.add(i2), PcFloat(5.5))

if __name__ == '__main__':
    unittest.main()

