class IterProduct:
    """
    Класс для итерации по списку товаров.
    """
    def __init__(self, category):
        """
        Инициализация экземпляров класса.
        :param category:
        """
        self.category = category

    def __iter__(self):
        self.current_value = -1
        return self

    def __next__(self):
        if self.current_value < len(self.category.products) - 1:
            self.current_value += 1
            return self.category.products[self.current_value]
        else:
            raise StopIteration
