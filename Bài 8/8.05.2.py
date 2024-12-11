print("Sinh vien: Le Van Nam")
print("MSSV: 235752021610085")
print("################################")
#########################################

import tkinter as tk

class MyApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Ứng Dụng với Indicators")
        self.root.geometry("400x300")

        self.check_var1 = tk.IntVar()
        self.check_var2 = tk.IntVar()
        self.check_var3 = tk.IntVar()
        self.check_var4 = tk.IntVar()
        self.check_var5 = tk.IntVar()
        self.check_button1 = tk.Checkbutton(self.root, text="Python", variable=self.check_var1, command=self.on_check_select)
        self.check_button2 = tk.Checkbutton(self.root, text="Perl", variable=self.check_var2, command=self.on_check_select)
        self.check_button3 = tk.Checkbutton(self.root, text="Java", variable=self.check_var3, command=self.on_check_select)
        self.check_button4 = tk.Checkbutton(self.root, text="C++", variable=self.check_var4, command=self.on_check_select)
        self.check_button5 = tk.Checkbutton(self.root, text="C", variable=self.check_var5, command=self.on_check_select)
        self.check_button1.pack()
        self.check_button2.pack()
        self.check_button3.pack()
        self.check_button4.pack()
        self.check_button5.pack()
        self.label = tk.Label(self.root, text="Chưa chọn lựa chọn nào")
        self.label.pack(pady=20)
    def on_check_select(self):
        selected = []
        if self.check_var1.get() == 1:
            selected.append("Python")
        if self.check_var2.get() == 1:
            selected.append("Perl")
        if self.check_var3.get() == 1:
            selected.append("Java")
        if self.check_var4.get() == 1:
            selected.append("C++")
        if self.check_var5.get() == 1:
            selected.append("C")
        if selected:
            self.label.config(text="Bạn đã chọn: " + ", ".join(selected))
        else:
            self.label.config(text="Chưa chọn lựa chọn nào")
root = tk.Tk()
app = MyApp(root)
root.mainloop()
