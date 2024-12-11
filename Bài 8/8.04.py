print("Sinh vien: Le Van Nam")
print("MSSV: 235752021610085")
print("################################")
#########################################

import tkinter as tk

class MyApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Ứng Dụng Tkinter: Thay Đổi Màu Nền và Màu Chữ")  
        self.root.geometry("400x300")  

        self.button = tk.Button(self.root, text="Nhấn tôi!", command=self.on_button_click, bg="lightblue", fg="black")
        self.button.pack(pady=20)

        self.label = tk.Label(self.root, text="Nhấn phím để thay đổi màu nền và màu chữ của nút!")
        self.label.pack(pady=20)

        self.root.bind("<Key>", self.on_key_press)

    def on_button_click(self):
        self.label.config(text="Nút đã được nhấn!")
    def on_key_press(self, event):
        pressed_key = event.keysym  
        
        if pressed_key == "r":  
            self.button.config(bg="red", fg="white")
            self.label.config(text="Màu nền và chữ của nút đã thay đổi thành màu đỏ!")
        elif pressed_key == "g":  
            self.button.config(bg="green", fg="white")
            self.label.config(text="Màu nền và chữ của nút đã thay đổi thành màu xanh!")
        elif pressed_key == "b":  
            self.button.config(bg="blue", fg="white")
            self.label.config(text="Màu nền và chữ của nút đã thay đổi thành màu xanh dương!")
        else:
            self.label.config(text=f"Bạn đã nhấn phím: {pressed_key}")
root = tk.Tk()
app = MyApp(root)  
root.mainloop()
