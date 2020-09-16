import unittest
import numpy as np
from unittest.mock import patch
from employee import Employee #importing Employee class from empolyee module

class TestEmployee(unittest.TestCase):
    
    def test_email(self):
        emp_1 = Employee('amri', 'vair', 10000)
        emp_2 = Employee('ram', 'gop', 10000)
        
        self.assertEqual(emp_1.email, 'amri.vair@gmail.com')
        self.assertEqual(emp_2.email, 'ram.gop@gmail.com')
        
        emp_1.first = 'nara'
        emp_2.first = 'raja'
        
        self.assertEqual(emp_1.email, 'nara.vair@gmail.com')
        self.assertEqual(emp_2.email, 'raja.gop@gmail.com')
        
    def test_monthly_schedule(self):
        with patch('employee.requests.get') as mocked_get:
            mocked_get.return_value.ok = True
            mocked_get.return_value.text = 'Success'

if __name__ == '__main__':
    unittest.main()