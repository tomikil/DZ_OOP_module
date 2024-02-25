class Product:
    """
    Класс для товаров
    """
    def __init__(self, name, description, price, quantity):
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
        return self.price * self.quantity + other.price * other.quantity

    @classmethod
    def create_products(cls, number):
        """
        Добавляеть новый товар
        :param number:
        :return:
        """
        return cls(**number)

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
