import unittest
import main

class TestChoppingList(unittest.TestCase):

    def test_state(self):
        result = main.salesTax('ma')
        self.assertEqual(result,{'Massachusett', [0.625]})


