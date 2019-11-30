import unittest
from employee import Employee

class TestEmployee(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print('setupClass')

    @classmethod
    def tearDownClass(cls):
        print('teardown class - runs only at end')

    def setUp(self):
        print('Runs before every test')

    def tearDown(self):
        print ('Runs after every test')

    def test_email(self):
        self.emp_1 = Employee('Rajitha','Smith',2000)
        self.emp_2 = Employee('Cori','Leah',3000)

        self.assertEqual(self.emp_1.email,'Rajitha.Smith@email.com')
        self.assertEqual(self.emp_2.email, 'Cori.Leah@email.com')
        self.assertNotEqual(self.emp_1.email,'Rajitha.Choudary@email.com')

        self.emp_1.last='Rogue'
        self.emp_2.last='Progue'

        self.assertEqual(self.emp_1.email,'Rajitha.Rogue@email.com')
        self.assertEqual(self.emp_2.email, 'Cori.Progue@email.com')


    def test_name(self):
        self.emp_1 = Employee('Ravi','Tuna',1300)
        self.emp_2 = Employee('Ashish','Ham',2400)

        self.assertEqual(self.emp_1.fullname,'Ravi Tuna')
        self.assertEqual(self.emp_2.fullname,'Ashish Ham')

        self.emp_1.last = 'Sharma'
        self.emp_2.last = 'Singh'

        self.assertEqual(self.emp_1.fullname,'Ravi Sharma')
        self.assertEqual(self.emp_2.fullname,'Ashish Singh')

    def test_get_raise(self):
        self.emp1 = Employee('Corey', 'Ronda', 1500)
        self.emp1.get_raise()
        self.assertNotEqual(self.emp1.pay,1500)
        self.assertEqual(self.emp1.pay, 1575)

if __name__ =='__main__':
    unittest.main()