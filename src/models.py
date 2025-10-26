class Product:
    """Класс продукт"""
    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity


class Category:
    """Класс категории продукта"""
    name: str
    description: str
    products: list
    category_count = 0
    product_count = 0

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.products = products if products is not None else []
        Category.category_count += 1
        Category.product_count += len(self.products)


if __name__ == '__main__':
    pr1 = Product('Помидор','Черри', 150, 50)
    pr2 = Product('Огурец','Гладкий', 100, 100)

    print(pr1.name)
    print(pr1.description)
    print(pr1.price)
    print(pr1.quantity)
    print('==========')
    vegetables = Category('vegetables', 'овощи', [pr1, pr2])
    print(vegetables.name)
    print(vegetables.description)
    print(vegetables.products)
    print(vegetables.category_count)
    print(vegetables.product_count)
