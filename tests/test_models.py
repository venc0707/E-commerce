from unittest.mock import patch

import pytest

from src.models import Category, Product


def test_product(first_product):
    assert first_product.name == "Samsung Galaxy S23 Ultra"
    assert first_product.price == 180000
    assert first_product.description == "256GB, Серый цвет, 200MP камера"
    assert first_product.quantity == 5


def test_category(first_category, first_product, second_product):
    assert first_category.name == "Смартфоны"
    assert (
        first_category.description
        == "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни"
    )
    assert first_category.category_count == 1
    assert first_category.product_count == 2


def test_private_list_products(first_product):
    cat1 = Category("Test", "tests", [first_product])
    assert cat1.name == "Test"
    assert cat1.description == "tests"
    assert cat1.products == "Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт.\n"


def test_add_product(first_category, new_product1):
    assert first_category.category_count == 1
    assert first_category.product_count == 2

    product_obj = Product(
        name=new_product1["name"],
        price=new_product1["price"],
        quantity=new_product1["quantity"],
        description=new_product1["description"],
    )
    first_category.add_product(product_obj)

    assert first_category.product_count == 3


def test_price(first_product, capsys):
    capsys.readouterr()
    first_product.price = -1
    captured = capsys.readouterr()
    assert captured.out == "Ошибка: Цена не может быть отрицательной (-1). Текущая цена: 180000.0\n"

    with patch("builtins.input", side_effect=["n"]):
        first_product.price = 1000
        assert first_product.price == 180000

    with patch("builtins.input", side_effect=["y"]):
        first_product.price = 1000
        assert first_product.price == 1000


def test_new_product(new_product1, first_category, new_product2):
    assert (
        first_category.products
        == "Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт.\nIphone 15, 210000.0 руб. Остаток: 8 шт.\n"
    )

    Product.new_product(new_product1, first_category)
    assert (
        first_category.products
        == "Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 10 шт.\nIphone 15, 210000.0 руб. Остаток: 8 шт.\n"
    )

    Product.new_product(new_product2, first_category)
    assert (
        first_category.products
        == "Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 10 шт.\nIphone 15, 210000.0 руб. Остаток: 8 шт.\nXiaomi Redmi Note 11, 31000.0 руб. Остаток: 14 шт.\n"
    )


def test_str_product(first_product):
    assert str(first_product) == "Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт."


def test_str_category(first_category):
    assert str(first_category) == "Смартфоны, количество продуктов: 13 шт."


def test_add_products(first_product, second_product):
    assert first_product + second_product == 2580000


def test_products_iter(product_iter):
    iter(product_iter)
    assert product_iter.index == 0
    assert next(product_iter).name == "Samsung Galaxy S23 Ultra"
    assert next(product_iter).name == "Iphone 15"

    with pytest.raises(StopIteration):
        next(product_iter)


def test_smartphone1(smartphone1):
    assert smartphone1.efficiency == 95.5
    assert smartphone1.model == "S23 Ultra"
    assert smartphone1.memory == 256
    assert smartphone1.color == "Серый"


def test_grass1(grass1):
    assert grass1.country == "Россия"
    assert grass1.germination_period == "7 дней"
    assert grass1.color == "Зеленый"


def test_smartphone_sum(smartphone1, smartphone2):
    smartphone_sum = smartphone1 + smartphone2
    assert smartphone_sum == 2580000.0


def test_invalid_sum(smartphone1, grass1):
    with pytest.raises(TypeError):
        smartphone1 + grass1


def test_add_no_product(first_category):
    with pytest.raises(TypeError):
        first_category.add_product("Not a product")


def test_print_mixin(capsys):
    Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    message = capsys.readouterr()
    assert message.out.strip() == 'Product(Samsung Galaxy S23 Ultra, 256GB, Серый цвет, 200MP камера, 180000.0, 5)'
