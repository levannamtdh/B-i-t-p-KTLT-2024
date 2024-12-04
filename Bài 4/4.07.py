print("Sinh vien: Le Van Nam")
print("MSSV: 235752021610085")
print("################################")
#########################################

input_string=input("nhap chuoi: ")
new_string=' '.join([char for char in input_string if not char.isdigit()])
print("chuoi moi sau khi loai bo chu so:",new_string)
