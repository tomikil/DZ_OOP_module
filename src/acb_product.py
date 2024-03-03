from abc import ABC, abstractmethod


class AbcProducts(ABC):
    @abstractmethod
    def __str__(self):
        pass

    @abstractmethod
    def __add__(self, other):
        pass

    @abstractmethod
    def price(self):
        pass

    @classmethod
    @abstractmethod
    def create_products(cls, product, list_product):
        pass
