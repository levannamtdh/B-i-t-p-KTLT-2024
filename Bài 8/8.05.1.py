print("Sinh vien: Le Van Nam")
print("MSSV: 235752021610085")
print("################################")
#########################################

import tkinter as tk

class MyApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Ứng Dụng Radio Button và Indicator")
        self.root.geometry("400x300")

        self.choice = tk.StringVar()

        self.radio_button1 = tk.Radiobutton(self.root, text="Python", variable=self.choice, value="Python", command=self.on_radio_select)
        self.radio_button2 = tk.Radiobutton(self.root, text="Perl", variable=self.choice, value="Perl", command=self.on_radio_select)
        self.radio_button3 = tk.Radiobutton(self.root, text="Java", variable=self.choice, value="Java", command=self.on_radio_select)
        self.radio_button4 = tk.Radiobutton(self.root, text="C++", variable=self.choice, value="C++", command=self.on_radio_select)
        self.radio_button5 = tk.Radiobutton(self.root, text="C", variable=self.choice, value="C", command=self.on_radio_select)
        self.radio_button1.pack()
        self.radio_button2.pack()
        self.radio_button3.pack()
        self.radio_button4.pack()
        self.radio_button5.pack()

        self.label = tk.Label(self.root, text="Chưa chọn lựa chọn nào")
        self.label.pack(pady=20)

    def on_radio_select(self):
        self.label.config(text=f"Bạn đã chọn: {self.choice.get()}")

root = tk.Tk()
app = MyApp(root)

root.mainloop()
