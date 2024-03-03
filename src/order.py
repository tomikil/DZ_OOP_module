from src.abc_category import AbcCategory


class Order(AbcCategory):
    def __init__(self, product, quantity_goods, total_cost):
        self.__product = product
        self.quantity_goods = quantity_goods
        self.total_cost = total_cost

    def __str__(self):
        return (f'Продукт: {self.__product.name}, Количество купленых товаров: {self.quantity_goods}, '
                f'Сумма заказа: {self.total_cost}')

    def __len__(self):
        return self.quantity_goods

    @property
    def products(self):
        return self.__product

    @classmethod
    def create_order(cls, products, list_product: list):
        for item in list_product:
            if products[0] == item.name:
                return cls(item, products[1], item.price * products[1])
