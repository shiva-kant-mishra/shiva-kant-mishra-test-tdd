import unittest
from string_calculator import add_string

class TestStringCalculator(unittest.TestCase):

    def test_add_string_empty_string_return_zero(self):
        self.assertEqual(add_string(''),0)

    def test_add_string_one_number_return_zero(self):
        self.assertEqual(add_string('5'),5)
        self.assertEqual(add_string('10'),10)

if __name__ == '__main__':
    unittest.main()