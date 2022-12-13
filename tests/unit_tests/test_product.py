import unittest
from prod.model.entity import *


class TestProduct(unittest.TestCase):   # если есть логика - тестим, 3 ветки + пограничные и внутр значения, отсутствие атрибута
    def test_setter_positive(self):
        product = Product()   # лучше pr
        product.price = 10

        expected = 10
        actual = product.price
        self.assertEqual(expected, actual)

    def test_setter_without_price(self):
        product = Product()  # дефолтный конструктор проверяем

        expected = 0
        actual = product.price
        self.assertEqual(expected, actual)

    def test_setter_negative(self):
        product = Product()  # дефолтный конструктор проверяем

        self.assertRaises(ValueError, product.price, -10)   #весь else можно заменить на это


        #self.assertRaises(ValueError, product.set_price, -10)


    ###############################################
        try:
            product.price = -10
            #self.fail()
            #raise AssertionError("It should ValueError...")
        except ValueError:
            pass
        else:
            self.fail("jhdfbgdg")  #генерация эксепшена вручную




if __name__ == "__main__":
    unittest.main()
