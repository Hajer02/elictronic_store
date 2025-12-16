# main.py
from prod import Product, Laptop, Phone, Headphone, Mouse, Keyboard, HardDisk



# ==========================================
# مسح المخزون بالكامل
# ==========================================
def clear_inventory():
    Product.all.clear()


# ==========================================
# إنشاء منتجات تجريبية
# ==========================================
def create_sample_inventory(clear_first=True):
    if clear_first:
        clear_inventory()

    Phone(
        "iPhone 12",
        3000,
        2200,
        1,
        condition="used",
        is_broken=False,
        battery_mah=3700,
        origin_country="China"
    )

    Laptop(
        "Dell Inspiron",
        5000,
        3500,
        3,
        condition="new",
        cpu_speed=3.0,
        ram_gb=16,
        storage_gb=512,
        origin_country="USA"
    )

    Headphone(
        "Sony WH-1000XM4",
        1200,
        1,
        brand="Sony",
        wireless=True,
        battery_hours=30,
        origin_country="Malaysia"
    )

    Mouse(
        "Logitech G102",
        150,
        5,
        dpi=8000,
        wireless=False,
        origin_country="China"
    )

    Keyboard(
        "Redragon K552",
        220,
        2,
        mechanical=True,
        backlit=True,
        layout="US",
        origin_country="China"
    )

    HardDisk(
        "Samsung T7",
        450,
        2,
        capacity_gb=1000,
        disk_type="SSD",
        interface="USB-C",
        origin_country="Korea"
    )


# ==========================================
# عرض المنتجات كنص
# ==========================================
def list_products_text():
    if not Product.all:
        return "📭 لا توجد منتجات حالياً.\n"

    out = "===== قائمة المنتجات =====\n"
    for p in Product.all:
        out += f"{p}\n"
    return out


# ==========================================
# تطبيق الخصم العادي على جميع المنتجات
# ==========================================
def apply_discount_all():
    for p in Product.all:
        p.apply_discount()


# ==========================================
# تطبيق خصم الزوجي (للكمية >= 2)
# ==========================================
def apply_pair_discount_all():
    for p in Product.all:
        p.apply_pair_discount()


# ==========================================
# تقرير شامل (عرض فقط)
# ==========================================
def run_inventory_logic():
    output = "\n===== تقرير النظام (عرض فقط) =====\n"

    if not Product.all:
        output += (
            "📭 لا توجد منتجات.\n"
            "اضغطي (إنشاء منتجات تجريبية) أو أضيفي منتجات يدوياً.\n"
        )
        return output

    output += "\n===== المنتجات الحالية =====\n"
    for item in Product.all:
        output += f"{item}\n"

    output += "\n===== ملاحظات =====\n"
    output += "ℹ هذا التقرير للعرض فقط ولا يغيّر الأسعار.\n"
    output += "✅ لتطبيق الخصم استخدمي زر (تطبيق خصم عادي) أو (تطبيق خصم زوجي).\n"


def run_inventory_logic():
    output = ""

    output += "\n===== إنشاء المنتجات =====\n"
    p1 = Phone("iPhone 12", 3000, 2200, 1, condition="used")
    p2 = Laptop("Dell Inspiron", 4500, 3000, 3, condition="new", cpu_speed=3.0)
    p3 = Headphone("Sony WH-1000XM4", 800, 2)
    p4 = Mouse("Logitech G102", 150, 5)
    p5 = Keyboard("Redragon K552", 200, 2)
    p6 = HardDisk("WD 1TB", 350, 1)

    output += "\n===== خصم شراء قطعتين =====\n"
    p3.apply_pair_discount()
    p5.apply_pair_discount()

    output += "\n===== كل المنتجات =====\n"
    for item in Product.all:
        output += f"{item}\n"


    return output