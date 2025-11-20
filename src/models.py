from  abc import  ABC, abstractmethod


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

    def __str__(self):
        count = 0
        for product in self.__products:
            count += product.quantity
        return f"{self.name}, количество продуктов: {count} шт."

    @property
    def products(self):
        """Возвращаем строку с описанием всех товаров"""
        if not self.__products:
            return "В этой категории нет товаров"
        return "\n".join(str(product) for product in self.__products) + "\n"

    def get_products_objects(self):
        """Возвращает список объектов товаров"""
        return self.__products

    def add_product(self, new_product):
        """Добавляет товар в категорию"""
        if isinstance(new_product, Product):
            self.__products.append(new_product)
            self.product_count += 1
        else:
            raise TypeError


class BaseProduct(ABC):

    @classmethod
    @abstractmethod
    def new_product(cls, *args, **kwargs):
        pass


class PrintMixin:
    def __init__(self):
        print(repr(self))

    def __repr__(self):
        return f'{self.__class__.__name__}({self.name}, {self.description}, {self.price}, {self.quantity})'


class Product(BaseProduct, PrintMixin):
    """Класс продукт"""

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity
        super().__init__()


    def __str__(self):
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        total_cost1 = self.__price * self.quantity
        total_cost2 = other.__price * other.quantity
        return total_cost1 + total_cost2

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


class Smartphone(Product):
    """Категории товаров «Смартфон»"""

    def __init__(self, name, description, price, quantity, efficiency, model, memory, color):
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color

    def __add__(self, other):
        if type(other) is Smartphone:
            return super().__add__(other)
        else:
            raise TypeError


class LawnGrass(Product):
    """Категории товаров «Трава газонная»"""

    def __init__(self, name, description, price, quantity, country, germination_period, color):
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color

    def __add__(self, other):
        if type(other) is LawnGrass:
            return super().__add__(other)
        else:
            raise TypeError


if __name__ == '__main__':
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    print(product1.name)
    print(product1.description)
    print(product1.price)
    print(product1.quantity)

    print(product2.name)
    print(product2.description)
    print(product2.price)
    print(product2.quantity)

    print(product3.name)
    print(product3.description)
    print(product3.price)
    print(product3.quantity)

    print('==Cat==')
    category1 = Category("Смартфоны",
                         "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
                         [product1, product2, product3])

    print(category1.name == "Смартфоны")
    print(category1.description)
    print(len(category1.products))
    print(category1.category_count)
    print(category1.product_count)

    product4 = Product("55\" QLED 4K", "Фоновая подсветка", 123000.0, 7)
    category2 = Category("Телевизоры",
                         "Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником",
                         [product4])

    print(category2.name)
    print(category2.description)
    print(len(category2.products))
    print(category2.products)

    print(Category.category_count)
    print(Category.product_count)