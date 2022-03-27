import unittest
from string_calculator import add_string

class TestStringCalculator(unittest.TestCase):

    def test_add_string_empty_string_return_zero(self):
        self.assertEqual(add_string(''),0)

    def test_add_string_one_number_return_number(self):
        self.assertEqual(add_string('5'),5)
        self.assertEqual(add_string('10'),10)
    
    def test_add_string_two_numbers_return_sum(self):
        self.assertEqual(add_string('5,10'),15)
        self.assertEqual(add_string('22,22'),44)
    
    def test_add_string_return_sum_of_n_numbers(self):
        self.assertEqual(add_string('5,10,20'),35)
        self.assertEqual(add_string('10,20,30,40,50'),150)

    def test_add_string_handle_newline_return_sum_of_n_numbers(self):
        self.assertEqual(add_string('5\n10,20'),35)
        self.assertEqual(add_string('10,20,30\n40,50'),150)

    def test_add_string_handle_any_delimiter_return_sum_of_n_numbers(self):
        self.assertEqual(add_string('//;\n5;10;20'),35)
        self.assertEqual(add_string('//-\n10-20-30\n40-50'),150)

    def test_add_string_negative_number_raise_value_error_with_number(self):
        with self.assertRaises(ValueError) as context:
            add_string('-5')
        self.assertEqual("negatives not allowed: -5",str(context.exception))
        with self.assertRaises(ValueError) as context:
            add_string('5,-10\n20')
        self.assertEqual("negatives not allowed: -10",str(context.exception))
        with self.assertRaises(ValueError) as context:
            add_string('5,-10\n20,-8,-9,12')
        self.assertEqual("negatives not allowed: -10 -8 -9 ",str(context.exception))
            

if __name__ == '__main__':
    unittest.main()