from product import Product


class Smartphone(Product):
    def __init__(self, name, description, price, quantity, color, performance, model, memory_capacity):

        self.performance = performance
        self.model = model
        self.memory_capacity = memory_capacity
        super().__init__(name, description, price, quantity, color)
