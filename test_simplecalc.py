
from simplecalc import simplecalc
import unittest

class TestPycom(unittest.TestCase):
    
    def calc(self, expr):
        ast = simplecalc(expr)
        return ast.value

    def test_num(self):
        self.assertEqual(self.calc("1"), 1)
        self.assertEqual(self.calc("12"), 12)

    def test_add(self):
        self.assertEqual(self.calc("2 + 3"), 5)

    def test_mul(self):
        self.assertEqual(self.calc("2 * 3"), 6)

    def test_space(self):
        self.assertEqual(self.calc("1+2"), 3)
        self.assertEqual(self.calc("1 + 2"), 3)
        self.assertEqual(self.calc("  1  +  2  "), 3)
        
    def test_null(self):
        self.assertRaises(SystemExit, self.calc, "")
        self.assertRaises(SystemExit, self.calc, " ")

    def test_string(self):
         self.assertRaises(SystemExit, self.calc, "a")

    def test_float(self):
        self.assertRaises(SystemExit, simplecalc, "1.5")

if __name__ == '__main__':
    unittest.main()

