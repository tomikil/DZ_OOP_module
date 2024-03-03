import pytest
import src.utils as utils
from src.product import Product
from src.category import Category

prod = [
    {
        "name": "Samsung Galaxy C23 Ultra",
        "description": "256GB, Серый цвет, 200MP камера",
        "price": 180000.0,
        "quantity": 5
    },
    {
        "name": "Iphone 15",
        "description": "512GB, Gray space",
        "price": 210000.0,
        "quantity": 8
    }
]

cat = {
    "name": "Смартфоны",
    "description": "Многофункциональное устройство",
    "products": [
        Product(prod[0].get("name"), prod[0].get("description"), prod[0].get("price"),
                prod[0].get("quantity")),
        Product(prod[1].get("name"), prod[1].get("description"), prod[1].get("price"),
                prod[1].get("quantity"))
    ]
}


@pytest.fixture
def product_all():
    return cat.get('products')


@pytest.fixture
def category():
    return Category(cat.get("name"), cat.get("description"), cat.get("products"))


def test_price(product_all):
    assert product_all[0].price == 180000.0
    product_all[0].price = 183000.0
    assert product_all[0].price == 183000.0
    product_all[0].price = 0
    assert product_all[0].price == 183000.0


def test_create_products(category, product_all):
    category.add_product(Product.create_products({"name": "Samsung Galaxy C23 Ultra",
                                                  "description": "256GB, Серый цвет, 200MP камера",
                                                  "price": 200000.0,
                                                  "quantity": 5
                                                  }, category.copy_product))
    assert product_all[0].quantity == 10
    assert product_all[0].price == 200000.0

    category.add_product(Product.create_products({"name": "Iphone 15 Pro MAX",
                                                  "description": "256GB, Синий",
                                                  "price": 190000.0,
                                                  "quantity": 7
                                                  }, category.copy_product))
    assert product_all[-1].quantity == 7
    assert product_all[-1].price == 190000.0

    category.add_product(Product.create_products({"name": "Samsung Galaxy C23 Ultra",
                                                  "description": "256GB, Серый цвет, 200MP камера",
                                                  "price": 150000.0,
                                                  "quantity": 5
                                                  }, category.copy_product))

    assert product_all[0].quantity == 15
    assert product_all[0].price == 200000.0


def test_add(product_all, category):
    assert product_all[0] + product_all[1] == 2580000.0
    with pytest.raises(TypeError):
        assert product_all[0] + category
