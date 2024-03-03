from abc import ABC, abstractmethod


class Goods(ABC):
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
    def create_products(cls, products):
        pass
