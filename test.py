from unittest import TestCase
import checkoutForTesting

class TestChoppingList(TestCase):

    def test_ma(self):
        result = checkoutForTesting.product('ma')
        self.assertEqual(result,(1450.2962499999999))

    def test_nh(self):
        result = checkoutForTesting.product('nh')
        self.assertEqual(result,(892.49))

    def test_me(self):
        result = checkoutForTesting.product('me')
        self.assertEqual(result,(1383.3595))

    def test_ME(self):
        result = checkoutForTesting.product('ME')
        self.assertEqual(result,(1383.3595))

    def test_New_Hampshire(self):
        result = checkoutForTesting.product('New Hampshire')
        self.assertEqual(result,(892.49))

    def test_Massachusett(self):
        result = checkoutForTesting.product('Massachusett')
        self.assertEqual(result,(1450.2962499999999))

    def test_Maine(self):
        result = checkoutForTesting.product('Maine')
        self.assertEqual(result,(1383.3595))

    def test_maine(self):
        result = checkoutForTesting.product('maine')
        self.assertEqual(result,(1383.3595))

    def test_randomInput(self):
        result = checkoutForTesting.product('AEFSWERF')
        self.assertEqual(result,('State Error, We only working with those following state: Massachusett, New Hampshire, Maine'))

    def test_NY(self):
        result = checkoutForTesting.product('NY')
        self.assertEqual(result,('State Error, We only working with those following state: Massachusett, New Hampshire, Maine'))