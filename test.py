import unittest
import main

class TestChoppingList(unittest.TestCase):

    def test_state(self):
        result = main.salesTax('ma')
        self.assertEqual(result,('Massachusett', 0.625))

    def test_state(self):
        result = main.salesTax('me')
        self.assertEqual(result,('new hampshire', 0.625))
        self.assertEqual(result,('maine', 0.55))



