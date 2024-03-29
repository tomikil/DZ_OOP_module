from src.acb_product import AbcProducts
from src.mixin_log import MixinLog


class Product(AbcProducts, MixinLog):
    """
    Класс для товаров
    """
    def __init__(self, name, description, price, quantity, color=None):
        """
        Инициализации элементов класса
        :param name: Наименования товара
        :param description:Описание товара
        :param price: Цена товара
        :param quantity: Колличество данного товара
        """
        self.name = name
        self.description = description
        self._price = price
        self.quantity = quantity
        self.color = color
        super().__init__()

    def __str__(self):
        """
        Информация о товаре в формате
        Продукт, X руб. Остаток: Y шт.
        :return:
        """
        return f"{self.name}, {self._price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        """
        Сладывает произведение цены и количество одного тоовара
        с произведение цены и количество второго товара
        :param other:
        :return:
        """
        if type(self) is not type(other):
            raise TypeError('Складывать можно только объекты Product или его наследников')
        return self.price * self.quantity + other.price * other.quantity

    @classmethod
    def create_products(cls, product: dict, list_product: list):
        """
        Добавляеть новый товар
        """
        for item in list_product:
            if item.name == product.get('name'):
                item.quantity += product.get('quantity')
                item.price = max(item.price, product.get('price'))
                print("\nЭтот товар уже есть на складе, количество в списке увеличено, цена выбрана наибольшая")

            return cls(**product)

    @property
    def price(self):
        """
        Геттер цены товара
        :return:
        """
        return self._price

    @price.setter
    def price(self, new_price):
        """
        Меняет цену товара
        :param new_price:
        :return:
        """
        float(new_price)
        if new_price <= 0.0:
            print('Цена введена не корректно!')
        elif new_price < self._price:
            answer = input('Цена ниже преждней. Вы хотите изменить цену (y/n):\n').lower()
            if answer == 'y':
                self._price = new_price
        else:
            self._price = new_price
