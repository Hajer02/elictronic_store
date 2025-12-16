
# مكتبات لمعالجة الكتابة العربية في الطرفية/الكونسول (اختياري)
import arabic_reshaper
from bidi.algorithm import get_display


# =====================================================
#                 CLASS Product (BASE)
# =====================================================
class Product:
    pay_rate = 0.8  # خصم افتراضي 20%
    all = []        # قائمة عامة لكل المنتجات

    def __init__(self, name, price, quantity, condition="new", origin_country=""):
        assert price > 0, "❌ السعر يجب أن يكون أكبر من صفر"
        assert quantity >= 0, "❌ الكمية يجب أن تكون 0 أو أكثر"

        self.name = name
        self.price = price
        self.quantity = quantity
        self.condition = condition  # new / used
        self.origin_country = origin_country  # بلد المنشأ (اختياري)

        Product.all.append(self)
        self.check_low_stock()

    # -----------------------------------------------------
    def calculate_total_price(self):
        return self.price * self.quantity

    # -----------------------------------------------------
    def apply_discount(self):
        self.price = self.price * self.pay_rate

    # -----------------------------------------------------
    def apply_pair_discount(self):
        if self.quantity >= 2:
            self.price = self.price * 0.90
            print(f"✔ تم تطبيق خصم شراء قطعتين على {self.name}")

    # -----------------------------------------------------
    def check_low_stock(self):
        if self.quantity <= 2:
            print(f"⚠ تحذير: المخزون منخفض للمنتج: {self.name}")

    # -----------------------------------------------------
    def __repr__(self):
        # نخليها عامة وبسيطة، والكلاسات الفرعية تقدر تزيد عليها
        origin = f" | Origin: {self.origin_country}" if self.origin_country else ""
        return f"{self.name} ({self.__class__.__name__}) | Price: {self.price} | Qty: {self.quantity}{origin}"

    # -----------------------------------------------------
    @classmethod
    def create_from_string(cls, data_string):
        """
        مثال:
        "iPhone,3000,5,new,China"
        """
        parts = data_string.split(",")
        name = parts[0]
        price = float(parts[1])
        qty = int(parts[2])
        condition = parts[3]
        origin_country = parts[4] if len(parts) > 4 else ""
        return cls(name, price, qty, condition, origin_country)


# =====================================================
#                   CLASS Laptop
# =====================================================
class Laptop(Product):
    pay_rate = 0.9  # خصم 10%

    def __init__(
        self,
        name,
        price_new,
        price_used,
        quantity,
        condition="new",
        cpu_speed=2.5,
        ram_gb=8,
        storage_gb=256,
        origin_country=""
    ):
        price = price_new if condition == "new" else price_used
        super().__init__(name, price, quantity, condition, origin_country)

        self.price_new = price_new
        self.price_used = price_used
        self.cpu_speed = cpu_speed
        self.ram_gb = ram_gb
        self.storage_gb = storage_gb

    def __repr__(self):
        base = super().__repr__()
        return f"{base} | CPU: {self.cpu_speed}GHz | RAM: {self.ram_gb}GB | Storage: {self.storage_gb}GB"


# =====================================================
#                   CLASS Phone
# =====================================================
class Phone(Product):
    def __init__(
        self,
        name,
        price_new,
        price_used,
        quantity,
        condition="new",
        is_broken=False,
        battery_mah=4000,
        origin_country=""
    ):
        price = price_new if condition == "new" else price_used
        super().__init__(name, price, quantity, condition, origin_country)

        self.price_new = price_new
        self.price_used = price_used
        self.is_broken = is_broken
        self.battery_mah = battery_mah

    def apply_discount(self):
        if self.is_broken:
            self.price *= 0.50
            print(f"✔ تم تطبيق خصم 50% (مكسور) على {self.name}")
        else:
            super().apply_discount()

    def __repr__(self):
        base = super().__repr__()
        broken = "Broken" if self.is_broken else "OK"
        return f"{base} | Battery: {self.battery_mah}mAh | State: {broken}"


# =====================================================
#     Accessories (بدل pass ضفنا خصائص)
# =====================================================

class Headphone(Product):
    def __init__(
        self,
        name,
        price,
        quantity,
        condition="new",
        brand="",
        wireless=False,
        battery_hours=0,
        origin_country=""
    ):
        super().__init__(name, price, quantity, condition, origin_country)
        self.brand = brand
        self.wireless = wireless
        self.battery_hours = battery_hours

    def __repr__(self):
        base = super().__repr__()
        w = "Wireless" if self.wireless else "Wired"
        brand = f"{self.brand}" if self.brand else "UnknownBrand"
        bat = f"{self.battery_hours}h" if self.wireless else "-"
        return f"{base} | Brand: {brand} | {w} | Battery: {bat}"


class Mouse(Product):
    def __init__(
        self,
        name,
        price,
        quantity,
        condition="new",
        dpi=800,
        wireless=False,
        origin_country=""
    ):
        super().__init__(name, price, quantity, condition, origin_country)
        self.dpi = dpi
        self.wireless = wireless

    def __repr__(self):
        base = super().__repr__()
        w = "Wireless" if self.wireless else "Wired"
        return f"{base} | DPI: {self.dpi} | {w}"


class Keyboard(Product):
    def __init__(
        self,
        name,
        price,
        quantity,
        condition="new",
        mechanical=False,
        backlit=False,
        layout="US",
        origin_country=""
    ):
        super().__init__(name, price, quantity, condition, origin_country)
        self.mechanical = mechanical
        self.backlit = backlit
        self.layout = layout

    def __repr__(self):
        base = super().__repr__()
        mech = "Mechanical" if self.mechanical else "Membrane"
        light = "Backlit" if self.backlit else "NoBacklight"
        return f"{base} | {mech} | {light} | Layout: {self.layout}"


class HardDisk(Product):
    def __init__(
        self,
        name,
        price,
        quantity,
        condition="new",
        capacity_gb=500,
        disk_type="HDD",     # HDD / SSD
        interface="USB",     # USB / SATA / NVMe ...
        origin_country=""
    ):
        super().__init__(name, price, quantity, condition, origin_country)
        self.capacity_gb = capacity_gb
        self.disk_type = disk_type
        self.interface = interface

    def __repr__(self):
        base = super().__repr__()
        return f"{base} | {self.disk_type} | {self.capacity_gb}GB | IF: {self.interface}"