from prod import Product, Laptop, Phone

if __name__ == "__main__":
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
