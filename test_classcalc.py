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
        self.assertRaises(IndexError, calc, '3.2')
        
    def test_string_add(self):
        self.assertEqual(calc('"abc" + "cde"'), 'abccde')
        
    def test_string_mul(self):
        self.assertEqual(calc('"abc" * 2'), 'abcabc')
        self.assertEqual(calc(' 3 * "abc"'), 'abcabcabc')
        
    def test_binop(self):
        data = [('1+2', 3),
                ('2*3', 6),
                ('5-2', 3),
                ('7/3', 2)
                ]
        for p in data:
            self.assertEquals(calc(p[0]), p[1], p[0]+' != '+str(p[1]))

    def test_variable(self):
        r = calcm('a= 3 * 2\n a-1')
        self.assertEqual(r[-1], 5)
        
if __name__ == '__main__':
    unittest.main()
