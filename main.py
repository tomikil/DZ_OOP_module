from src.category import Category
from src.product import Product
import src.utils as utils
from src.order import Order

file = 'products.json'

conect = utils.filling_classes(utils.connection_file(file))

conect[0].add_product(Product.create_products({"name": "Samsung Galaxy C23 Ultra",
                                               "description": "256GB, Серый цвет, 200MP камера",
                                               "price": 183000.0,
                                               "quantity": 4
                                               }, conect[0].copy_product))

order = Order.create_order(('Samsung Galaxy C23 Ultra', 2), conect[0].copy_product)
print(f'\n{order}')





