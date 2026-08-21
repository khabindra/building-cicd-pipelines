from django.test import TestCase

from .views import add_numbers


class CalculatorTests(TestCase):
    def test_add_numbers(self):
        result = add_numbers(2, 3)
        self.assertEqual(result, 6)
