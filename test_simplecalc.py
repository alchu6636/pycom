
import simplecalc
import unittest

class TestScanner(unittest.TestCase):
    def scan(self, string):
        return simplecalc.SimpleScanner().tokenize(string)
        
    def test_num(self):
        tokens = self.scan('2 333')
        self.assertEqual(len(tokens), 2)
        self.assertEqual(tokens[0].attr, '2')
        self.assertEqual(tokens[1].attr, '333')
    
    def test_string(self):
        tokens = self.scan(' "a" "b c" "5" " " ""')
        self.assertEqual(len(tokens), 5)
        self.assertEqual(tokens[0].attr, '"a"')
        self.assertEqual(tokens[1].attr, '"b c"')
        self.assertEqual(tokens[2].attr, '"5"')
        self.assertEqual(tokens[3].attr, '" "')
        self.assertEqual(tokens[4].attr, '""')
        
class TestPycom(unittest.TestCase):
    
    def calc(self, expr):
        ast = simplecalc.simplecalc(expr)
        return ast.value

    def test_num(self):
        self.assertEqual(self.calc('1'), 1)
        self.assertEqual(self.calc('12'), 12)

    def test_add(self):
        self.assertEqual(self.calc('2 + 3'), 5)

    def test_mul(self):
        self.assertEqual(self.calc('2 * 3'), 6)

    def test_space(self):
        self.assertEqual(self.calc('1+2'), 3)
        self.assertEqual(self.calc('1 + 2'), 3)
        self.assertEqual(self.calc('  1  +  2  '), 3)
        
    def test_null(self):
        self.assertRaises(SystemExit, self.calc, '')
        self.assertRaises(SystemExit, self.calc, ' ')

    def test_string(self):
        self.assertRaises(SystemExit, self.calc, 'a')

    def test_float(self):
        self.assertRaises(SystemExit, self.calc, '1.5')

class TestCalcString(unittest.TestCase):
    def calc(self, expr):
        ast = simplecalc.simplecalc(expr)
        return ast.value

    def test_factor(self):
        self.assertEqual(self.calc('"abc"'), 'abc')

    def test_add(self):
        self.assertEqual(self.calc('"a" + "bc"'), 'abc')
        self.assertEqual(self.calc('"a" + "bc" + "def"'), 'abcdef')

    def test_mul1(self):
        self.assertEqual(self.calc('"a" * 3'), 'aaa')
        self.assertEqual(self.calc('3 * "a"'), 'aaa')
        self.assertEqual(self.calc('2 * "a" * 3'), 'aaaaaa')
        
    def test_mul_error(self):
        self.assertRaises(TypeError, self.calc, '"a" * "b"')
        
        
if __name__ == '__main__':
    unittest.main()

