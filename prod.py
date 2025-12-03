

class Product:
    pay_rate = 0.8
    all = []

    def _init_(self, name, price, quantity, prod_date):
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

    def _repr_(self):
        return f"Product('{self.name}', {self.price}, {self.quantity})"

    @classmethod
    def create_from_string(cls, data_string):
        name, price, quantity, prod_date = data_string.split(',')
        return cls(name, float(price), int(quantity), prod_date)


class Laptop(Product):
    pay_rate = 0.9

    def _init_(self, name, price, quantity, prod_date, cpu_speed):
        super()._init_(name, price, quantity, prod_date)
        assert cpu_speed > 2, f"CPU speed {cpu_speed} is too low!"
        self.cpu_speed = cpu_speed

    def _repr_(self):
        return f"Laptop('{self.name}', {self.price}, {self.quantity}, {self.cpu_speed}GHz)"


class Phone(Product):
    def _init_(self, name, price, quantity, prod_date, is_broken=False):
        super()._init_(name, price, quantity, prod_date)
        self.is_broken = is_broken

    def apply_discount(self):
        if self.is_broken:
            self.price = self.price * 0.8
        else:
            super().apply_discount()

    def _repr_(self):
        return f"Phone('{self.name}', {self.price}, {self.quantity}, Broken={self.is_broken})"


# الجزء التنفيذي
if __name__ == "_main_":
    p1 = Product("Keyboard", 50, 5, "2025-01-01")
    p2 = Laptop("Dell Inspiron", 1500, 2, "2025-02-10", 3.5)
    p3 = Phone("iPhone 13", 3500, 1, "2025-03-15", is_broken=True)
    p4 = Product.create_from_string("Mouse,20,4,2025-02-01")

    p1.apply_discount()
    p2.apply_discount()
    p3.apply_discount()

    print("\n🧾 قائمة المنتجات:")
    for item in Product.all:
        print(item)

    print("\n💰 الإجمالي:", p1.calculate_total_price())
    print("📦 كل المنتجات:", Product.all)