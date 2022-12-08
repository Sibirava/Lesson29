from prod.model.entity import *

class ShopAssistance:
    @staticmethod
    def calculate_total_price(basket):
        if not isinstance(basket, Basket):
            return -1

        total = 0

        for i in range(basket.size()):
            product = basket.get(i)
            if isinstance(product, Product):
                total += product.price

        return total