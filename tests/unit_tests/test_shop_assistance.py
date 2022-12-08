import unittest

from prod.model.entity import *
from prod.model.logic import *

class TestShopAssistance(unittest.TestCase):

    def test_calculate_total_price_basic(self):
        basket = Basket()
        basket.add(Product(1.5))
        basket.add(Product(2.5))
        basket.add(Product(3.5))
        expected = 7.5

        actual = ShopAssistance.calculate_total_price(basket)

        self.assertEqual(expected, actual)

    # ......str, bool
    def test_calculate_total_price_with_incorrect_data(self):
        expected = -1
        actual = ShopAssistance.calculate_total_price(10)

        self.assertEqual(expected, actual)

    def test_calculate_total_price_with_empty_basket(self):
        expected = 0
        actual = ShopAssistance.calculate_total_price(Basket())

        self.assertEqual(expected, actual)

    def test_calculate_total_price_with_only_one_product(self):
        basket = Basket()
        product = Product(10)
        basket.add(product)
        expected = product.price

        actual = ShopAssistance.calculate_total_price(basket)
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()