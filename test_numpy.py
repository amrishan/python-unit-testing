#naming convention for test is test_ whatever you are testing
import unittest
import numpy as np

#inheriting form unittest.TestCase class for 
#useful test cases
class TestCalc(unittest.TestCase):
    
    def test_sum(self):
        #test for edge cases
        #Write good test cases not many
        self.assertEqual(np.sum([10, 5]), 15)
        self.assertEqual(np.sum([-1, 1]), 0)
        self.assertEqual(np.sum([-1, -1]), -2)
    
    def test_subtract(self):
        self.assertEqual(np.subtract(10, 5), 5)
        self.assertEqual(np.subtract(-1, 1), -2)
        self.assertEqual(np.subtract(-1, -1), 0)
    
    def test_multiply(self):
        self.assertEqual(np.multiply(10, 5), 50)
        self.assertEqual(np.multiply(-1, 1), -1)
        self.assertEqual(np.multiply(-1, -1), 1)
    
    def test_divide(self):
        self.assertEqual(np.divide(10, 5), 2)
        self.assertEqual(np.divide(-1, 1), -1)
        self.assertEqual(np.divide(-1, -1), 1)
        
        #use context manager to test exceptions
        with self.assertRaises(ValueError):
            np.divide(2, 0)
        
        
if __name__ == '__main__':
    unittest.main()