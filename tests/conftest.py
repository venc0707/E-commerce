import pytest
from src.models import Product, Category


@pytest.fixture
def first_product():
    return Product('Помидор','Черри', 150, 50)


@pytest.fixture
def second_product():
    return Product('Огурец','Гладкий', 100, 100)


@pytest.fixture
def first_category(first_product, second_product):
    return Category('vegetables', 'овощи', [first_product, second_product])
