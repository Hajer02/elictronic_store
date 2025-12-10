from datetime import datetime

class SmartDiscountEngine:

    def _init_(self):
        self.messages = []  # تجميع رسائل الخصم لكل منتج

    def apply(self, product, customer=None):
        """تطبيق الخصومات الذكية وإرجاع السعر النهائي + الرسائل"""
        self.messages = []
        original_price = product.price

        price = original_price

        # -------------------------------
        # 1) خصم حسب حالة المنتج
        # -------------------------------
        if product.condition == "used":
            price *= 0.90
            self.messages.append("✔ خصم 10% (منتج مستعمل)")

        if hasattr(product, "is_broken") and product.is_broken:
            price *= 0.50
            self.messages.append("✔ خصم 50% (منتج مكسور)")

        # -------------------------------
        # 2) مخزون منخفض
        # -------------------------------
        if product.quantity == 1:
            price *= 0.75
            self.messages.append("✔ خصم 25% (آخر قطعة!)")

        elif product.quantity <= 3:
            price *= 0.95
            self.messages.append("✔ خصم 5% (مخزون قليل)")

        # -------------------------------
        # 3) خصم حسب الوقت (Happy Hour)
        # -------------------------------
        hour = datetime.now().hour
        if 18 <= hour <= 22:
            price *= 0.80
            self.messages.append("✔ خصم المساء 20%")

        # -------------------------------
        # 4) خصم حسب الشركة المصنعة
        # -------------------------------
        brand = product.name.split()[0].lower()

        brand_discounts = {
            "apple": 0.95,     # خصم 5%
            "samsung": 0.90,   # خصم 10%
            "dell": 0.93,      # خصم 7%
            "sony": 0.92       # خصم 8%
        }

        if brand in brand_discounts:
            price *= brand_discounts[brand]
            self.messages.append(f"✔ خصم شركة {brand.title()}")

        # -------------------------------
        # 5) خصم موسمي
        # -------------------------------
        seasonal = 0.90  # 10%
        price *= seasonal
        self.messages.append("✔ خصم موسمي 10%")

        # -------------------------------
        # 6) نقاط العميل (Loyalty)
        # -------------------------------
        if customer:
            if customer.points > 100:
                price *= 0.90
                self.messages.append("✔ خصم ولاء العملاء 10%")
            elif customer.points > 50:
                price *= 0.95
                self.messages.append("✔ خصم ولاء العملاء 5%")

        # -------------------------------
        # 7) خصم ذكي حسب قدم المنتج في المخزون
        # -------------------------------
        if hasattr(product, "days_in_stock") and product.days_in_stock > 60:
            price *= 0.85   # 15%
            self.messages.append("✔ خصم 15% (منتج قديم في المخزون)")

        # -------------------------------
        # إرجاع النتائج
        # -------------------------------
        return price, self.messages