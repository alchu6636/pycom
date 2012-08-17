
import simplecalc
import unittest

class TestPycom(unittest.TestCase):

    def test_init(self):
        ast = simplecalc.simplecalc("2 + 3")
        self.assertEqual(ast.value, 5)

if __name__ == '__main__':
    unittest.main()

        
