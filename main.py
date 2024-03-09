from src.category import Category
from src.product import Product
import src.utils as utils
from src.order import Order
from src.lawn_grass import LawnGrass

file = 'products.json'

conect = utils.filling_classes(utils.connection_file(file))

# conect[0].add_product(Product.create_products({"name": "1Samsung Galaxy C23 Ultra",
#                                                "description": "256GB, Серый цвет, 200MP камера",
#                                                "price": 183000.0,
#                                                "quantity": 0
#                                                }, conect[0].copy_product))

order = Order.create_order(('Samsung Galaxy C23 Ultra', 0), conect[0].copy_product)
print(f'\n{order}')
#
# conect[0].add_product(LawnGrass.create_products({
#     "name": 'grass',
#     "description": 'grass',
#     "price": 4500,
#     "quantity": 0,
#     "color": 'Зеленый',
#     "manufacturer_country": 'gggg',
#     "germination_period": 'aaa'
# }, conect[0].copy_product))





