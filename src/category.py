from src.product import Product
from src.abc_category import AbcCategory


class Category(AbcCategory):
    """
    Класс для хранения категории товаров
    """
    quantity_category = 0
    quantity_unique_products = 0

    def __init__(self, name, description, product):
        """
        Метод для инициализации экземпляров класса
        :param name: название категории товаров
        :param description: описание категории товаров
        :param product: Список товаров
        """

        self.name = name
        self.description = description
        self.__product = product
        super().__init__()
        Category.quantity_category += 1
        Category.quantity_unique_products += len(self.__product)

    def __len__(self):
        """
        Общее количество товаров в категории
        :return:
        """
        return sum(product.quantity for product in self.__product)

    def __str__(self):
        """
        Информация о категории с общем количеством товаров в формате
        Продукт, количество продуктов: Х шт.
        :return:
        """
        return f"{self.name}, количество продуктов: {len(self)} шт."

    def add_product(self, products: object):
        """
        Добавление обьекта класса Product в список категории
        :param products:
        :return:
        """
        if not isinstance(products, Product):
            raise TypeError("Добавлять можно только объекты Product или его наследников")

        Category.quantity_unique_products += 1
        return self.__product.append(products)

    @property
    def products(self):
        """
        Список с обьектами класса Продукт
        :return:
        """
        return self.__product

    @property
    def copy_product(self):
        list_product = []
        for product in self.__product:
            list_product.append(product)
        return list_product
