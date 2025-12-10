from prod import *
from smart_discount import SmartDiscountEngine

def run_inventory_logic():
    output = "\n=== نظام الخصومات الذكي ===\n"

    engine = SmartDiscountEngine()

    products = [
        Phone("iPhone 12", 3000, 2200, 1, condition="used"),
        Laptop("Dell Inspiron", 5000, 3500, 3, condition="new"),
        Headphone("Sony WH-1000XM4", 1200, 800, 5)
    ]

    for p in products:
        final_price, msgs = engine.apply(p)

        output += f"\n{p.name}\n"
        output += f"السعر الأصلي: {p.price}\n"
        output += "الخصومات المطبقة:\n"

        for m in msgs:
            output += f"{m}\n"

        output += f"💰 السعر النهائي: {round(final_price, 2)}\n"
        output += "---------------------------\n"

    return output