import classcalc
import unittest

def calc(s):
    calc = classcalc.Calc()
    calc.run_string(s)
    return calc.result[-1]
    
def calcm(s):
    slist = s.split('\n')
    calc = classcalc.Calc()
    for line in slist:
        calc.run_string(line)
    return calc.result

class TestCalc(unittest.TestCase):
        
    def test_int(self):
        self.assertEqual(calc('3'), 3)

    def test_float(self):
        self.assertEqual(calc('3.2'), 3.2)
        self.assertEqual(calc('.5'), 0.5)

    def test_string(self):
        self.assertEqual(calc('"abc"'), 'abc')

    def test_int_add_int(self):
        self.assertEqual(calc('3 .add(0)'), 3) # need space following int

    def test_int_mul_int(self):
        self.assertEqual(calc('4 .mul(1)'), 4)

    def test_float_add_int(self):
        self.assertEqual(calc('1.25.add(0)'), 1.25)

    def test_float_mul_int(self):
        self.assertEqual(calc('1.25.mul(1)'), 1.25)

    def test_str_add_str(self):
        self.assertEqual(calc('"abc".add("")'), 'abc')

    def test_str_mul_int(self):
        self.assertEqual(calc('"abc".mul(1)'), 'abc')

if __name__ == '__main__':
    unittest.main()
