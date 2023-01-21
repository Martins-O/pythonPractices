from unittest import TestCase

from function.is_palindrome import is_palindrome


class Test(TestCase):
    def test_is_palindrome(self):
        word = is_palindrome('madam')
        self.assertTrue(word)
