from unittest import TestCase
from unittest import mock
import checkout

class TestChoppingList(TestCase):
    @mock.patch('checkout.input', create=True)

    def test_MA(self, mocked_input):
        mocked_input.side_effect = ['ma']
        result = checkout.salesTax()
        self.assertEqual(result,('Massachusett', 0.625))

    @mock.patch('checkout.input', create=True)
    def test_ME(self, mocked_input):
        mocked_input.side_effect = ['me']
        result = checkout.salesTax()
        self.assertEqual(result,('Maine', 0.55))

    @mock.patch('checkout.input', create=True)
    def test_NH(self, mocked_input):
        mocked_input.side_effect = ['NH']
        result = checkout.salesTax()
        self.assertEqual(result,('New Hampshire', 0))

    @mock.patch('checkout.input', create=True)
    def test_product(self, mocked_input):
        mocked_input.side_effect=['1', 'apple']
        result = checkout.product()
        self.assertEqual(result, ('apple', '$', 2.99))



    #def test_exists(self):