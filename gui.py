# gui.py
import tkinter as tk
from main import run_inventory_logic  # 👈 استيراد الدالة من main

# إنشاء النافذة
window = tk.Tk()
window.title("إدارة المخزون")
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

# تشغيل النافذة
window.mainloop()

