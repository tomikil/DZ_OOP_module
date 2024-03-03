from src.category import Category
from src.product import Product
import src.utils as utils

file = 'products.json'

conect = utils.filling_classes(utils.connection_file(file))

conect[0].add_product(Product.create_products({"name": "Iphone 15 Pro MAX",
                                               "description": "1024GB, Синий",
                                               "price": 31000.0,
                                               "quantity": 4
                                               }))
