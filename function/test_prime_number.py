from unittest import TestCase

from function.prime_number import is_prime


class Test(TestCase):
    def test_is_prime(self):
        number = is_prime(90)
        self.assertFalse(number)
