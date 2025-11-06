class Category:
    """Класс категории продукта"""
    category_count = 0
    product_count = 0

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.__products = products if products is not None else []
        Category.category_count += 1
        Category.product_count += len(self.__products)

    @property
    def products(self):
        """Возвращаем строку с описанием всех товаров"""
        product_str = ""
        for product in self.__products:
            product_str += f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт.\n"

        return product_str

    def get_products_objects(self):
        """Возвращает список объектов товаров"""
        return self.__products

    def add_product(self, new_product):
        """Добавляет товар в категорию"""
        self.__products.append(new_product)
        self.product_count += 1


class Product:
    """Класс продукт"""

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    @property
    def price(self):
        """Возвращает цену на продукт"""
        return self.__price

    @price.setter
    def price(self, new_price):
        """Проверяет цену"""
        old_price = self.__price

        if new_price < 0:
            print(f"Ошибка: Цена не может быть отрицательной ({new_price}). Текущая цена: {old_price}")

        if new_price > 0:
            if new_price < old_price:
                user_input = input(
                    f'"согласия понизить цену", текущая цена: {old_price} => {new_price} y - да, n - нет:  '
                ).lower()
                if user_input == "y":
                    self.__price = new_price

    @classmethod
    def new_product(cls, new_pr, category):
        """Создает новый продукт или обновляет существующий в категории"""

        existing_products = category.get_products_objects()

        new_name = new_pr["name"]
        new_description = new_pr["description"]
        new_price = new_pr["price"]
        new_quantity = new_pr["quantity"]

        duplicates = []
        for product in existing_products:
            if product.name.lower == new_name.lower:
                duplicates.append(product)

        if duplicates:
            existing_products = duplicates[0]
            existing_products.quantity += new_quantity
            existing_products.price = max(existing_products.price, new_price)

            return existing_products
        else:
            new_product = cls(name=new_name, description=new_description, price=new_price, quantity=new_quantity)

            existing_products.append(new_product)
            return new_product


if __name__ == "__main__":
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    category1 = Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
        [product1, product2, product3],
    )

    print(category1.products)
    product4 = Product('55" QLED 4K', "Фоновая подсветка", 123000.0, 7)
    category1.add_product(product4)
    print(category1.products)
    print(category1.product_count)

    new_product = Product.new_product(
        {
            "name": "Samsung Galaxy S23 Ultra",
            "description": "256GB, Серый цвет, 200MP камера",
            "price": 180000.0,
            "quantity": 5,
        },
        category1,
    )

    print(new_product.name)
    print(new_product.description)
    print(new_product.price)
    print(new_product.quantity)

    print("======")
    new_product.price = 800
    print(new_product.price)
    print("======")

    new_product.price = -100
    print(new_product.price)
    print(category1.products)

    new_product.price = 0
    print(new_product.price)

    print(category1.products)
