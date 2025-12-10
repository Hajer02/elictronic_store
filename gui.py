import tkinter as tk

# إنشاء النافذة
window = tk.Tk()
window.title("إدارة المخزون")
window.geometry("400x300")

# عنوان
label = tk.Label(window, text="مرحبًا بك في نظام إدارة المخزون", font=("Arial", 14))
label.pack(pady=20)

# زر
button = tk.Button(window, text="خروج", command=window.quit)
button.pack(pady=10)

# تشغيل النافذة
window.mainloop()