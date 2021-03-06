"""unit test for Calculate class"""

# This file was created on 17/09/2017
# Author: George Kaimakis - https://github.com/geokai

import unittest

import _mypath
from calculate import Calculate


class TestCalculate(unittest.TestCase):
    """unittest class"""

    def setUp(self):
        """set-up method - create a 'Calculate' object"""
        self.calc = Calculate()

    def test_add_method_returns_correct_result(self):
        """add method test - assertEqual"""
        self.assertEqual(4, self.calc.add(2, 2))

    def test_add_method_raises_typeerror_if_not_ints(self):
        """test for correct 'Raise' for type error"""
        self.assertRaises(TypeError, self.calc.add, 'Hello', 'World')


if __name__ == '__main__':
    unittest.main()
