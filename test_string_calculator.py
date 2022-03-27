import unittest
from string_calculator import StringCalculator

class TestStringCalculator(unittest.TestCase):

    def test_add_string_empty_string_return_zero(self):
        sc = StringCalculator()
        self.assertEqual(sc.add_string(''),0)


if __name__ == '__main__':
    unittest.main()