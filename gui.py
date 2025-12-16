# gui.py
import tkinter as tk
<<<<<<< HEAD
from tkinter import simpledialog, messagebox
=======
from main import run_inventory_logic  # 👈 استيراد الدالة من main
>>>>>>> 4e425c2c18938025fbbf5b1ba404efd9fdbbe3e8

from main import (
    create_sample_inventory,
    list_products_text,
    apply_discount_all,
    apply_pair_discount_all,
    clear_inventory,
    run_inventory_logic
)

from prod import Phone, Laptop, Headphone, Mouse, Keyboard, HardDisk


# ==========================================
# إنشاء النافذة الرئيسية
# ==========================================
window = tk.Tk()
window.title("إدارة المخزون")
<<<<<<< HEAD
window.geometry("650x520")


label = tk.Label(window, text="نظام إدارة المخزون", font=("Arial", 16))
label.pack(pady=10)


text_box = tk.Text(window, wrap=tk.WORD, height=18, width=75)
text_box.pack(pady=10)


def show_text(txt):
    text_box.delete(1.0, tk.END)
    text_box.insert(tk.END, txt)


# ==========================================
# أزرار التحكم
# ==========================================
def btn_create_samples():
    create_sample_inventory(clear_first=True)
    show_text("✅ تم إنشاء منتجات تجريبية.\n\n" + list_products_text())


def btn_list_products():
    show_text(list_products_text())


def btn_discount_all():
    apply_discount_all()
    show_text("✅ تم تطبيق الخصم العادي.\n\n" + list_products_text())


def btn_pair_discount_all():
    apply_pair_discount_all()
    show_text("✅ تم تطبيق خصم الزوجي.\n\n" + list_products_text())


def btn_clear():
    clear_inventory()
    show_text("🧹 تم مسح كل المنتجات من المخزون.")


def btn_report():
    show_text(run_inventory_logic())


# ==========================================
# إضافة منتج جديد (مع خصائص الإكسسوارات)
# ==========================================
def btn_add_product():
    kind = simpledialog.askstring(
        "إضافة منتج",
        "اكتبي نوع المنتج:\nphone / laptop / headphone / mouse / keyboard / harddisk"
    )
    if not kind:
        return
    kind = kind.strip().lower()

    name = simpledialog.askstring("اسم المنتج", "اكتبي اسم المنتج:")
    if not name:
        return

    qty = simpledialog.askinteger("الكمية", "اكتبي الكمية:", minvalue=0)
    if qty is None:
        return

    origin = simpledialog.askstring("بلد المنشأ", "اكتبي بلد المنشأ (اختياري):")
    origin = (origin or "").strip()


    # =====================
    # Phone
    # =====================
    if kind == "phone":
        price_new = simpledialog.askfloat("سعر الجديد", "اكتبي سعر الجديد:", minvalue=0.0)
        price_used = simpledialog.askfloat("سعر المستعمل", "اكتبي سعر المستعمل:", minvalue=0.0)
        condition = simpledialog.askstring("الحالة", "new أو used ؟")
        if not condition:
            return
        condition = condition.strip().lower()

        broken = messagebox.askyesno("مكسور؟", "هل الهاتف مكسور؟")
        battery = simpledialog.askinteger("Battery", "اكتبي سعة البطارية (mAh):", minvalue=0)
        if battery is None:
            battery = 0

        Phone(
            name,
            price_new,
            price_used,
            qty,
            condition=condition,
            is_broken=broken,
            battery_mah=battery,
            origin_country=origin
        )


    # =====================
    # Laptop
    # =====================
    elif kind == "laptop":
        price_new = simpledialog.askfloat("سعر الجديد", "اكتبي سعر الجديد:", minvalue=0.0)
        price_used = simpledialog.askfloat("سعر المستعمل", "اكتبي سعر المستعمل:", minvalue=0.0)
        condition = simpledialog.askstring("الحالة", "new أو used ؟")
        if not condition:
            return
        condition = condition.strip().lower()

        cpu = simpledialog.askfloat("CPU Speed", "اكتبي سرعة المعالج (مثلاً 3.0):", minvalue=0.0)
        ram = simpledialog.askinteger("RAM", "اكتبي الرام (GB):", minvalue=0)
        storage = simpledialog.askinteger("Storage", "اكتبي التخزين (GB):", minvalue=0)

        Laptop(
            name,
            price_new,
            price_used,
            qty,
            condition=condition,
            cpu_speed=cpu if cpu is not None else 0.0,
            ram_gb=ram if ram is not None else 0,
            storage_gb=storage if storage is not None else 0,
origin_country=origin
        )


    # =====================
    # Headphone
    # =====================
    elif kind == "headphone":
        price = simpledialog.askfloat("السعر", "اكتبي السعر:", minvalue=0.0)
        brand = simpledialog.askstring("Brand", "اكتبي الماركة (اختياري):")
        wireless = messagebox.askyesno("Wireless؟", "هل هي لاسلكية؟")

        battery_hours = 0
        if wireless:
            bh = simpledialog.askinteger("Battery Hours", "كم ساعة بطارية؟", minvalue=0)
            battery_hours = bh if bh is not None else 0

        Headphone(
            name,
            price,
            qty,
            brand=(brand or "").strip(),
            wireless=wireless,
            battery_hours=battery_hours,
            origin_country=origin
        )


    # =====================
    # Mouse
    # =====================
    elif kind == "mouse":
        price = simpledialog.askfloat("السعر", "اكتبي السعر:", minvalue=0.0)
        dpi = simpledialog.askinteger("DPI", "اكتبي DPI (مثلاً 8000):", minvalue=0)
        wireless = messagebox.askyesno("Wireless؟", "هل الماوس لاسلكي؟")

        Mouse(
            name,
            price,
            qty,
            dpi=dpi if dpi is not None else 800,
            wireless=wireless,
            origin_country=origin
        )


    # =====================
    # Keyboard
    # =====================
    elif kind == "keyboard":
        price = simpledialog.askfloat("السعر", "اكتبي السعر:", minvalue=0.0)
        mechanical = messagebox.askyesno("Mechanical؟", "هل الكيبورد ميكانيكي؟")
        backlit = messagebox.askyesno("Backlit؟", "هل فيه إضاءة؟")
        layout = simpledialog.askstring("Layout", "اكتبي Layout (مثلاً US / AR):")
        layout = (layout or "US").strip()

        Keyboard(
            name,
            price,
            qty,
            mechanical=mechanical,
            backlit=backlit,
            layout=layout,
            origin_country=origin
        )


    # =====================
    # HardDisk
    # =====================
    elif kind == "harddisk":
        price = simpledialog.askfloat("السعر", "اكتبي السعر:", minvalue=0.0)
        capacity = simpledialog.askinteger("Capacity (GB)", "اكتبي السعة بالـ GB (مثلاً 1000):", minvalue=0)
        disk_type = simpledialog.askstring("Type", "HDD أو SSD ؟")
        interface = simpledialog.askstring("Interface", "واجهة التوصيل (USB / SATA / NVMe ...):")

        HardDisk(
            name,
            price,
            qty,
            capacity_gb=capacity if capacity is not None else 0,
            disk_type=(disk_type or "HDD").strip().upper(),
            interface=(interface or "USB").strip(),
            origin_country=origin
        )


    else: 
        messagebox.showerror("خطأ", "نوع غير معروف. اكتبي مثل: phone أو laptop ...")
        return

    show_text("✅ تمت إضافة المنتج.\n\n" + list_products_text())


# ==========================================
# إطار الأزرار
# ==========================================
btn_frame = tk.Frame(window)
btn_frame.pack(pady=5)

tk.Button(btn_frame, text="إنشاء منتجات تجريبية", command=btn_create_samples, width=18)\
    .grid(row=0, column=0, padx=5, pady=5)

tk.Button(btn_frame, text="عرض المنتجات", command=btn_list_products, width=18)\
    .grid(row=0, column=1, padx=5, pady=5)

tk.Button(btn_frame, text="تطبيق خصم عادي", command=btn_discount_all, width=18)\
    .grid(row=0, column=2, padx=5, pady=5)

tk.Button(btn_frame, text="تطبيق خصم زوجي", command=btn_pair_discount_all, width=18)\
    .grid(row=1, column=0, padx=5, pady=5)

tk.Button(btn_frame, text="تقرير كامل (عرض فقط)", command=btn_report, width=18)\
    .grid(row=1, column=1, padx=5, pady=5)

tk.Button(btn_frame, text="مسح المخزون", command=btn_clear, width=18)\
    .grid(row=1, column=2, padx=5, pady=5)

tk.Button(btn_frame, text="إضافة منتج", command=btn_add_product, width=18)\
    .grid(row=2, column=1, padx=5, pady=5)

tk.Button(window, text="خروج", command=window.quit, width=15).pack(pady=8)
=======
window.geometry("500x400")

# عنوان
label = tk.Label(window, text="نظام إدارة المخزون", font=("Arial", 16))
label.pack(pady=10)

# صندوق النصوص لعرض النتائج
text_box = tk.Text(window, wrap=tk.WORD, height=15, width=55)
text_box.pack(pady=10)

# دالة لعرض النتائج عند الضغط على الزر
def show_results():
    results = run_inventory_logic()   # استدعاء كود main
    text_box.delete(1.0, tk.END)      # مسح القديم
    text_box.insert(tk.END, results)  # عرض النتائج

# زر لعرض النتائج
run_button = tk.Button(window, text="عرض النتائج", command=show_results)
run_button.pack(pady=5)

# زر خروج
exit_button = tk.Button(window, text="خروج", command=window.quit)
exit_button.pack(pady=5)
>>>>>>> 4e425c2c18938025fbbf5b1ba404efd9fdbbe3e8

window.mainloop()