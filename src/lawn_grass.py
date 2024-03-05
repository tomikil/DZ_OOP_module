from src.product import Product


class LawnGrass(Product):
    def __init__(self, name, description, price, quantity, color, manufacturer_country, germination_period):

        self.manufacturer_country = manufacturer_country
        self.germination_period = germination_period
        super().__init__(name, description, price, quantity, color)
