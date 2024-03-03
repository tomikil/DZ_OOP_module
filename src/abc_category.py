from abc import ABC, abstractmethod


class AbcCategory(ABC):

    @abstractmethod
    def __str__(self):
        pass

    @abstractmethod
    def __len__(self):
        pass

    @abstractmethod
    def products(self):
        pass
