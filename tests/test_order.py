import pytest
from src.product import Product
from src.category import Category
from src.order import Order
from exception import ProductQuantityZeroError

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


def test_create_order(category):
    order = Order.create_order(('Samsung Galaxy C23 Ultra', 2), category.copy_product)
    assert str(order) == 'Продукт: Samsung Galaxy C23 Ultra, Количество купленых товаров: 2, Сумма ' 'заказа: 360000.0'


def test_len(category):
    order = Order.create_order(('Samsung Galaxy C23 Ultra', 2), category.copy_product)
    assert order.__len__() == 2


def test_products(category):
    order = Order("Samsung Galaxy", 2, 360_000.0)
    assert order.products == 'Samsung Galaxy'


def test_create_order_error(category):
    with pytest.raises(ProductQuantityZeroError) as e_info:
        assert Order.create_order(('Samsung Galaxy C23 Ultra', 0), category.copy_product)
