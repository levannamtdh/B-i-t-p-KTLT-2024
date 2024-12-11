print("Sinh vien: Le Van Nam")
print("MSSV: 235752021610085")
print("################################")
#########################################

import tkinter as tk
from tkinter import messagebox

def show_selection():
    selected_option = var.get()  
    if selected_option == 1:
        result_label.config(text="Lựa chọn: 1")
    elif selected_option == 2:
        result_label.config(text="Lựa chọn: 2")
    elif selected_option == 3:
        result_label.config(text="Lựa chọn: 3")
    else:
        result_label.config(text="Chưa chọn!")

root = tk.Tk()
root.title("Thông Tin Cá Nhân")
root.geometry("500x400")

frame_info = tk.Frame(root)
frame_info.pack(pady=20)

label_name = tk.Label(frame_info, text="Họ và tên:")
label_name.grid(row=0, column=0, padx=10, pady=5, sticky="e")
entry_name = tk.Entry(frame_info, width=30)
entry_name.grid(row=0, column=1, padx=10, pady=5)

label_birthday = tk.Label(frame_info, text="Ngày sinh (dd/mm/yyyy):")
label_birthday.grid(row=1, column=0, padx=10, pady=5, sticky="e")
entry_birthday = tk.Entry(frame_info, width=30)
entry_birthday.grid(row=1, column=1, padx=10, pady=5)

label_mssv = tk.Label(frame_info, text="MSSV:")
label_mssv.grid(row=2, column=0, padx=10, pady=5, sticky="e")
entry_mssv = tk.Entry(frame_info, width=30)
entry_mssv.grid(row=2, column=1, padx=10, pady=5)

label_major = tk.Label(frame_info, text="Ngành học:")
label_major.grid(row=3, column=0, padx=10, pady=5, sticky="e")
entry_major = tk.Entry(frame_info, width=30)
entry_major.grid(row=3, column=1, padx=10, pady=5)

frame_radio = tk.Frame(root)
frame_radio.pack(pady=20)

var = tk.IntVar()

radio1 = tk.Radiobutton(frame_radio, text="First", variable=var, value=1)
radio1.pack(anchor="w")
radio2 = tk.Radiobutton(frame_radio, text="Second", variable=var, value=2)
radio2.pack(anchor="w")
radio3 = tk.Radiobutton(frame_radio, text="Third", variable=var, value=3)
radio3.pack(anchor="w")

button = tk.Button(frame_radio, text="Click Me", command=show_selection)
button.pack(pady=10)

result_label = tk.Label(root, text="Lựa chọn: Chưa chọn!", font=("Helvetica", 14))
result_label.pack(pady=20)

root.mainloop()
