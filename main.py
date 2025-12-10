from prod import Product, Laptop, Phone, Headphone, Mouse, Keyboard, HardDisk

print("\n===== إنشاء المنتجات =====")

p1 = Phone("iPhone 12", 3000, 2200, 1, condition="used")
p2 = Laptop("Dell Inspiron", 4500, 3000, 3, condition="new", cpu_speed=3.0)
p3 = Headphone("Sony WH-1000XM4", 800, 2)
p4 = Mouse("Logitech G102", 150, 5)
p5 = Keyboard("Redragon K552", 200, 2)
p6 = HardDisk("WD 1TB", 350, 1)

print("\n===== خصم شراء قطعتين =====")
p3.apply_pair_discount()
p5.apply_pair_discount()

print("\n===== كل المنتجات =====")
for item in Product.all:
    print(item)