import unittest
import numpy as np
from unittest.mock import patch
from employee import Employee #importing Employee class from empolyee module

class TestEmployee(unittest.TestCase):
    """
    Test Driven Development is where you write the test
    before you write the code
    """
    
    @classmethod
    def setUpClass(cls):
        #runs only once before all test
        print('setUpClass first')
    
    @classmethod
    def tearDownClass(cls):
        #runs only once after all test
        print('\ntearDownClass last')

    def setUp(self):
        """
        this method runs before every test
        the tests dont usually run in order
        tests should be isolated from on another
        """
        self.emp_1 = Employee('amri', 'vair', 10000)
        self.emp_2 = Employee('ram', 'gop', 10000)
    
    def tearDown(self):
        pass
        
    def test_email(self):
        self.assertEqual(self.emp_1.email, 'amri.vair@gmail.com')
        self.assertEqual(self.emp_2.email, 'ram.gop@gmail.com')
        
        self.emp_1.first = 'nara'
        self.emp_2.first = 'raja'
        
        self.assertEqual(self.emp_1.email, 'nara.vair@gmail.com')
        self.assertEqual(self.emp_2.email, 'raja.gop@gmail.com')
        
    def test_monthly_schedule(self):
        with patch('employee.requests.get') as mocked_get:
            mocked_get.return_value.ok = True
            mocked_get.return_value.text = 'Success'
            
            #schedule = self.emp_1.monthly_schedule('May')
            #mocked_get.assert_called_with('http://company.com/Schafer/may')
            #self.assertEqual(schedule, 'Success')
            

if __name__ == '__main__':
    unittest.main()