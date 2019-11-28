import unittest
import calc


# create test class

class TestCalc(unittest.TestCase):
    ## write method to test method
    def test_add(self):
       result = calc.add(10,5)
       self.assertEqual(result,15)

    ## Testing the exceptions
    def test_divide(self):
        self.assertRaises(ValueError, calc.divide,10,0)

if __name__=='__main__':
    unittest.main()