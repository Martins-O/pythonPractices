from unittest import TestCase

from function.adding import *


class Test(TestCase):
    def test_add(self):
        addition = add(2, 3)
        self.assertEquals(5, addition)

    def test_subtract(self):
        subtraction = subtract(55, 25)
        self.assertEquals(30, subtraction)

    def test_multiply(self):
        multiplication = multiply(2, 3)
        self.assertEquals(6, multiplication)

    def test_divide(self):
        division = divide(6, 2)
        self.assertEquals(3, division)

    def test_modulo(self):
        modulo = mod(6, 2)
        self.assertEqual(0, modulo)

    def test_power(self):
        powers = power(2, 3)
        self.assertEquals(8, powers)
