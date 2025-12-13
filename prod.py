
import arabic_reshaper
from bidi.algorithm import get_display

class Product:
    pay_rate = 0.8        # خصم افتراضي 20%
    all = []

    def __init__(self, name, price, quantity, condition="new"):
        assert price > 0, "❌ السعر يجب أن يكون أكبر من صفر"
        assert quantity >= 0, "❌ الكمية يجب أن تكون 0 أو أكثر"

        self.name = name
        self.price = price
        self.quantity = quantity
        self.condition = condition  # new / used

       

        Product.all.append(self)

        self.check_low_stock()

 
    def calculate_total_price(self):
        return self.price * self.quantity

    
    def apply_discount(self):
        self.price = self.price * self.pay_rate

    
    def apply_pair_discount(self):
        if self.quantity >= 2:
            self.price = self.price * 0.90
            print(f"✔ تم تطبيق خصم شراء قطعتين على {self.name}")

    
    def check_low_stock(self):
        if self.quantity <= 2:
            print(f"⚠ تحذير: المخزون منخفض للمنتج: {self.name}")

    def __repr__(self):
        return f"{self.name} | Price: {self.price} | Qty: {self.quantity}"

   
    @classmethod
    def create_from_string(cls, data_string):
        parts = data_string.split(",")
        name = parts[0]
        price = float(parts[1])
        qty = int(parts[2])
        condition = parts[3]
        return cls(name, price, qty, condition)


class Laptop(Product):
    pay_rate = 0.9

    def __init__(self, name, price_new, price_used, quantity, condition="new", cpu_speed=2.5):
        price = price_new if condition == "new" else price_used
        super().__init__(name, price, quantity, condition)
        self.price_new = price_new
        self.price_used = price_used
        self.cpu_speed = cpu_speed


class Phone(Product):

    def __init__(self, name, price_new, price_used, quantity, condition="new", is_broken=False):
        price = price_new if condition == "new" else price_used
        super().__init__(name, price, quantity, condition)

        self.price_new = price_new
        self.price_used = price_used
        self.is_broken = is_broken

    def apply_discount(self):
        if self.is_broken:
            self.price *= 0.50
            print(f"✔ تم تطبيق خصم 50% (مكسور) على {self.name}")
        else:
            super().apply_discount()



class Headphone(Product):
    pass

class Mouse(Product):
    pass

class Keyboard(Product):
    pass

class HardDisk(Product):
    pass