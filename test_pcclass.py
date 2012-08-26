from pcclass import PcInt, PcFloat
import unittest

class TestLiteral(unittest.TestCase):
    def setUp(self):
        self.i0 = PcInt(0)
        self.i1 = PcInt(1)
        self.i2 = PcInt(2)
        self.f2 = PcFloat(2.0)
        self.f05 = PcFloat(0.5)

    def test_str(self):
        self.assertEqual(str(self.i0), '0')
        self.assertEqual(str(self.f2), '2.0')

    def test_add(self):
        self.assertEqual(self.i1.add(self.i2), PcInt(3))
        self.assertEqual(self.i1.add(self.f2), PcFloat(3))
        self.assertEqual(self.f2.add(self.i1), PcFloat(3))
        self.assertEqual(self.f2.add(self.f05), PcFloat(2.5))

    def test_add_int(self):
        self.assertEqual(self.i2._add_int(self.i1), PcInt(3))
        self.assertEqual(self.f2._add_int(self.i1), PcFloat(3.0))
        
    def test_add_float(self):
        self.assertEqual(self.i1._add_float(self.f2), PcFloat(3))
        self.assertEqual(self.f05._add_float(self.f2), PcFloat(2.5))


if __name__ == '__main__':
    unittest.main()

