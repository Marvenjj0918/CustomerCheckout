from unittest import TestCase
import checkoutForTestingPurpusing

class TestChoppingList(TestCase):

    def test_ma(self):
        result = checkoutForTestingPurpusing.product('ma')
        self.assertEqual(result,(1450.2962499999999))

    def test_nh(self):
        result = checkoutForTestingPurpusing.product('nh')
        self.assertEqual(result,(892.49))

    def test_me(self):
        result = checkoutForTestingPurpusing.product('me')
        self.assertEqual(result,(1383.3595))

    def test_ME(self):
        result = checkoutForTestingPurpusing.product('ME')
        self.assertEqual(result,(1383.3595))

    def test_New_Hampshire(self):
        result = checkoutForTestingPurpusing.product('New Hampshire')
        self.assertEqual(result,(892.49))

    def test_Massachusett(self):
        result = checkoutForTestingPurpusing.product('Massachusett')
        self.assertEqual(result,(1450.2962499999999))

    def test_Maine(self):
        result = checkoutForTestingPurpusing.product('Maine')
        self.assertEqual(result,(1383.3595))

    def test_maine(self):
        result = checkoutForTestingPurpusing.product('maine')
        self.assertEqual(result,(1383.3595))

    def test_randomInput(self):
        result = checkoutForTestingPurpusing.product('AEFSWERF')
        self.assertEqual(result,('State Error, We only working with those following state: Massachusett, New Hampshire, Maine'))

    def test_NY(self):
        result = checkoutForTestingPurpusing.product('NY')
        self.assertEqual(result,('State Error, We only working with those following state: Massachusett, New Hampshire, Maine'))