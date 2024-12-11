print("Sinh vien: Le Van Nam")
print("MSSV: 235752021610085")
print("################################")
#########################################

import tkinter as tk
from tkinter import filedialog, messagebox

class MyApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Ứng Dụng Menu Tkinter")
        self.root.geometry("500x400")

        self.menu_bar = tk.Menu(self.root)

        self.file_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.file_menu.add_command(label="New", command=self.new_file)
        self.file_menu.add_command(label="Open", command=self.open_file)
        self.file_menu.add_separator()  
        self.file_menu.add_command(label="Exit", command=self.exit_app)

        self.edit_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.edit_menu.add_command(label="Insert Text", command=self.insert_text)
        self.edit_menu.add_command(label="Insert Picture", command=self.insert_picture)

        self.help_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.help_menu.add_command(label="About", command=self.about)

        self.menu_bar.add_cascade(label="File", menu=self.file_menu)
        self.menu_bar.add_cascade(label="Edit", menu=self.edit_menu)
        self.menu_bar.add_cascade(label="Help", menu=self.help_menu)

        self.root.config(menu=self.menu_bar)

        self.label = tk.Label(self.root, text="Chọn một mục từ menu", pady=20)
        self.label.pack()

    def new_file(self):
        self.label.config(text="Đã chọn New File!")
        print("New File được tạo")

    def open_file(self):
        filename = filedialog.askopenfilename(title="Open File")
        if filename:
            self.label.config(text=f"Đã chọn file: {filename}")
        else:
            self.label.config(text="Không có file nào được chọn")

    def exit_app(self):
        self.label.config(text="Thoát ứng dụng...")
        print("Đóng ứng dụng")
        self.root.quit()

    def insert_text(self):
        self.label.config(text="Đã chọn Insert Text!")
        print("Chèn văn bản")

    def insert_picture(self):
        filename = filedialog.askopenfilename(title="Insert Picture", filetypes=[("Image files", "*.png;*.jpg;*.jpeg;*.gif")])
        if filename:
            self.label.config(text=f"Đã chọn hình ảnh: {filename}")
        else:
            self.label.config(text="Không có hình ảnh nào được chọn")

    def about(self):
        messagebox.showinfo("About", "Ứng dụng Tkinter Menu\nPhiên bản 1.0")

root = tk.Tk()

app = MyApp(root)

root.mainloop()
