import classcalc
import unittest

def calc(s):
    calc = classcalc.Calc()
    calc.run_string(s)
    return calc.result[-1]
    
class TestCalc(unittest.TestCase):
        
    def test_num(self):
        self.assertEqual(calc('3'), 3)
        
    def test_add(self):
        self.assertEqual(calc('3 + 23'), 26)

    def test_lines(self):
        calc = classcalc.Calc()
        calc.run_string('3')
        calc.run_string('2')
        self.assertEqual(calc.result[0], 3)
        self.assertEqual(calc.result[1], 2)
        
        
#    def test_var(self):
#        self.assertEqual(calc('a=3'), 7)

if __name__ == '__main__':
    unittest.main()
