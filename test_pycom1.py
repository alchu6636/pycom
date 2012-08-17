
from simplecalc import simplecalc
import unittest

class TestPycom(unittest.TestCase):

    def test_add(self):
        ast = simplecalc("2 + 3")
        self.assertEqual(ast.value, 5)

    def test_mul(self):
        ast = simplecalc("2*3")
        self.assertEqual(ast.value, 6)

    def test_string(self):
        self.assertRaises(SystemExit, simplecalc, "a")

    def test_num(self):
        ast = simplecalc("1")
        self.assertEqual(ast.value, 1)
        ast = simplecalc("12")
        self.assertEqual(ast.value, 12)

    def test_float(self):
        self.assertRaises(SystemExit, simplecalc, "1.5")

if __name__ == '__main__':
    unittest.main()

