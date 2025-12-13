from prod import Product, Laptop, Phone, Headphone, Mouse, Keyboard, HardDisk

def run_inventory_logic():
    output = "" 
    output += "\n===== إنشاء المنتجات =====\n"

    p1 = Phone("iPhone 12", 3000, 2200, 1, condition="used")
    p2 = Laptop("Dell Inspiron", 5000, 3500, 3, condition="new", cpu_speed=3.0)
    p3 = Headphone("Sony WH-1000XM4", 1200, 800, 1)
    p4 = Mouse("Logitech G102", 150, 100, 5)

    products = [p1, p2, p3, p4]

    # تطبيق الخصومات
    for item in products:
        before = item.price
        item.apply_discount()
        after = item.price

        output += f"\n{item.name}: السعر قبل = {before} ، بعد الخصم = {after}\n"

    # تطبيق خصم شراء قطعتين
    for item in products:
        before = item.price
        item.apply_pair_discount()

        if item.quantity >= 2:
            output += f"✔ تم تطبيق خصم زوجي على {item.name}\n"

    # عرض ملخص نهائي
    output += "\n===== ملخص المنتجات =====\n"
    for item in products:
        output += f"{item}\n"

    return output