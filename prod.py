
import arabic_reshaper
from bidi.algorithm import get_display
class Product:
    pay_rate = 0.8
    all = []

    def __init__(self, name:str, price:float, quantity:int, prod_date):
        assert price >= 0, f"Price {price} is not valid!"
        assert quantity >= 0, f"Quantity {quantity} is not valid!"
        self.name = name
        self.price = price
        self.quantity = quantity
        self.prod_date = prod_date
        Product.all.append(self)

    def calculate_total_price(self):
        return self.price * self.quantity

    def apply_discount(self):
        self.price = self.price * self.pay_rate

    def __repr__(self):
        return f"Product('{self.name}', {self.price}, {self.quantity})"

    @classmethod
    def create_from_string(cls, data_string):
        name, price, quantity, prod_date = data_string.split(',')
        return cls(name, float(price), int(quantity), prod_date)


class Laptop(Product):
    pay_rate = 0.9

    def __init__(self, name, price, quantity, prod_date, cpu_speed):
        super().__init__(name, price, quantity, prod_date)
        assert cpu_speed > 2, f"CPU speed {cpu_speed} is too low!"
        self.cpu_speed = cpu_speed

    def __repr__(self):
        return f"Laptop('{self.name}', {self.price}, {self.quantity}, {self.cpu_speed}GHz)"


class Phone(Product):
    def __init__(self, name:str, price:float, quantity, prod_date, is_broken=False):
        super().__init__(name, price, quantity, prod_date)
        self.is_broken = is_broken

    def apply_discount(self):
        if self.is_broken:
            self.price = self.price * 0.8
        else:
            super().apply_discount()

    def __repr__(self):
        return f"Phone('{self.name}', {self.price}, {self.quantity}, Broken={self.is_broken})"
