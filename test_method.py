import classcalc
import unittest
import operator

class TestMethod(unittest.TestCase):

    def add(self, obj, arg):
        try:
            return operator.add(obj, arg)
#            return obj.add(arg)
        except TypeError:
            return "TypeError"

    def mul(self, obj, arg):
        try:
            return operator.mul(obj, arg)
#            return obj.mul(arg)
        except TypeError:
            return "TypeError"
    
    def test_add(self):
        op = self.add
        self.assertEqual(op(2, 3), 5)
        self.assertEqual(op(2, 3.1), 5.1)
        self.assertEqual(op(2, "b"), "TypeError")
        self.assertEqual(op(2.1, 3), 5.1)
        self.assertEqual(op(2.1, 3.0), 5.1)
        self.assertEqual(op(2.1, "b"), "TypeError")
        self.assertEqual(op("a", 3), "TypeError")
        self.assertEqual(op("a", 3.0), "TypeError")
        self.assertEqual(op("a", "b"), "ab")

        
        
    def test_mul(self):
        op = self.mul
        self.assertEqual(op(2, 3), 6)
        self.assertEqual(op(2, 3.1), 2.0 * 3.1)
        self.assertEqual(op(2, "b"), "bb")
        self.assertEqual(op(2.1, 3), 2.1 * 3.0)
        self.assertEqual(op(2.1, 3.0), 2.1 * 3.0)
        self.assertEqual(op(2.1, "b"), "TypeError")
        self.assertEqual(op("a", 3), "aaa")
        self.assertEqual(op("a", 3.0), "TypeError")
        self.assertEqual(op("a", "b"), "TypeError")        
        
if __name__ == '__main__':
    unittest.main()

