import pytest
import src.utils as utils
from src.product import Product
from src.iter_product import IterProduct

file = './products.json'


@pytest.fixture
def category():
    return utils.filling_classes(utils.connection_file(file))


def test_iter_product(category):
    assert [product.name for product in IterProduct(category[0])] == ['Samsung Galaxy C23 Ultra', 'Iphone 15', 'Xiaomi Redmi Note 11']