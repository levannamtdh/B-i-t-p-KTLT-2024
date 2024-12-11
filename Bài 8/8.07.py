print("Sinh vien: Le Van Nam")
print("MSSV: 235752021610085")
print("################################")
#########################################

import tkinter as tk
import random
import time


colors = ['red', 'green', 'blue', 'yellow', 'orange', 'pink', 'purple', 'brown', 'black', 'white']
color_names = ['Red', 'Green', 'Blue', 'Yellow', 'Orange', 'Pink', 'Purple', 'Brown', 'Black', 'White']

class ColorGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Game Học Màu Tiếng Anh")
        self.root.geometry("500x400")

        self.score = 0
        self.time_left = 120  
        self.current_color = None

        self.score_label = tk.Label(self.root, text=f"Điểm: {self.score}", font=("Helvetica", 16))
        self.score_label.pack(pady=10)

        self.color_label = tk.Label(self.root, text="", font=("Helvetica", 40), width=20, height=2)
        self.color_label.pack(pady=50)

        self.entry = tk.Entry(self.root, font=("Helvetica", 16))
        self.entry.pack(pady=10)

        self.check_button = tk.Button(self.root, text="Kiểm tra", font=("Helvetica", 16), command=self.check_answer)
        self.check_button.pack(pady=10)

        self.time_label = tk.Label(self.root, text=f"Thời gian còn lại: {self.time_left}s", font=("Helvetica", 16))
        self.time_label.pack(pady=10)

        self.update_color()
        self.update_timer()

    def update_color(self):
        color_index = random.randint(0, len(colors) - 1)
        self.current_color = colors[color_index]
        color_name = color_names[color_index]

        self.color_label.config(text=color_name, fg=self.current_color)

    def check_answer(self):
        user_answer = self.entry.get().strip().lower()

        if user_answer == self.current_color:
            self.score += 2  
        else:
            self.score -= 1  

        self.score_label.config(text=f"Điểm: {self.score}")
        self.entry.delete(0, tk.END)  
        self.update_color()  

    def update_timer(self):
        if self.time_left > 0:
            self.time_left -= 1
            self.time_label.config(text=f"Thời gian còn lại: {self.time_left}s")
            self.root.after(1000, self.update_timer)  
        else:
            self.end_game()

    def end_game(self):
        
        self.color_label.config(text="Thời gian đã hết!", fg="black")
        self.check_button.config(state="disabled")  
        messagebox.showinfo("Kết thúc", f"Trò chơi kết thúc! Điểm của bạn là: {self.score}")
        self.root.quit()

root = tk.Tk()

game = ColorGame(root)

root.mainloop()
