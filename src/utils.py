import json

from src.models import Category, Product


def open_file_json(path_file: str):
    """открытие json файла"""
    with open(path_file, "r", encoding="utf-8") as f:
        return json.load(f)


def create_class_obj(data: list[dict]):
    """Создает обьекты классов"""
    list_categories = []
    list_products = []
    for category in data:
        list_categories.append(Category(**category))
        for product in category["products"]:
            list_products.append(Product(**product))
    return list_categories, list_products


if __name__ == "__main__":
    open_file = open_file_json("../data/products.json")
    create_class_obj(open_file)
