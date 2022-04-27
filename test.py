import unittest
import main

class TestChoppingList(unittest.TestCase):

    def test_state(self):
        result = main.salesTax()
        if sta
        self.assertEqual(result,('Massachusett', 0.625))

    def test_state(self):
        result = main.salesTax('me')
        self.assertEqual(result,('Maine', 0.55))

    def test_state(self):
        result = main.salesTax()
        self.assertEqual(result,('New Hampshire', 0))



