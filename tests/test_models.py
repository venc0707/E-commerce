import pytest
from src.models import Category, Product


def test_product(first_product):
    assert first_product.name == 'Помидор'
    assert first_product.price == 150
    assert first_product.description == 'Черри'
    assert first_product.quantity == 50


def test_category(first_category, first_product, second_product):
    assert first_category.name == 'vegetables'
    assert first_category.description == 'овощи'
    assert first_category.category_count == 1
    assert first_category.product_count == 2