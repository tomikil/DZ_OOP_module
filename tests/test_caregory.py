import pytest
import src.utils as utils
from src.product import Product
from src.category import Category
from src.lawn_grass import LawnGrass

file = './products.json'


@pytest.fixture
def category():
    return utils.filling_classes(utils.connection_file(file))


@pytest.fixture
def raise_category():
    return Category("Смартфоны", "Лучший дизайн", [
        Product('Samsung Galaxy C23 Ultra', '256GB, Серый цвет, 200MP камера', 0, 0, None),
        Product('Iphone 15', '512GB, Gray space', 0, 0, None),
        Product('Xiaomi Redmi Note 11', '1024GB, Синий', 0, 0, None)
    ])


def test_add_product(category):
    assert Category.quantity_unique_products == 4
    category[0].add_product(Product('Iphone 13', '512GB, Gray space', 150000, 10))
    assert Category.quantity_unique_products == 5
    with pytest.raises(TypeError):
        assert category[0].add_product(category)


def test_proucts(category):
    assert str(category[0].products[0]) == 'Samsung Galaxy C23 Ultra, 180000.0 руб. Остаток: 5 шт.'
    assert str(category[0].products[2]) == 'Xiaomi Redmi Note 11, 31000.0 руб. Остаток: 14 шт.'


def test_len(category):
    assert len(category[0]) == 27


def test_str(category):
    assert str(category[0]) == 'Смартфоны, количество продуктов: 27 шт.'


def test_ValueError(category):
    with pytest.raises(ValueError) as e_info:
        category[0].add_product(LawnGrass.create_products({
            "name": 'grass',
            "description": 'grass',
            "price": 4500,
            "quantity": 0,
            "color": 'Зеленый',
            "manufacturer_country": 'gggg',
            "germination_period": 'aaa'
        }, category[0].copy_product))


def test_get_average_price_goods(category):
    assert category[0].get_average_price_goods() == 140333.3


def test_get_average_price_goods_zero_division_category(raise_category):
    assert raise_category.get_average_price_goods() == 0.0
