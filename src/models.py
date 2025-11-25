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

    def middle_price(self):
        """ подсчитывает средний ценник всех товаров категории """
        try:
            return sum([product.price for product in self.__products]) / len(self.__products)
        except ZeroDivisionError:
            return 0


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
        if quantity == 0:
            raise ValueError('Товар с нулевым количеством не может быть добавлен')
        else:
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
    try:
        product_invalid = Product("Бракованный товар", "Неверное количество", 1000.0, 0)
    except ValueError as e:
        print(
            "Возникла ошибка ValueError прерывающая работу программы при попытке добавить продукт с нулевым количеством")
    else:
        print("Не возникла ошибка ValueError при попытке добавить продукт с нулевым количеством")

    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    category1 = Category("Смартфоны", "Категория смартфонов", [product1, product2, product3])

    print(category1.middle_price())

    category_empty = Category("Пустая категория", "Категория без продуктов", [])
    print(category_empty.middle_price())