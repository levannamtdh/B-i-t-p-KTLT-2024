print("Sinh vien: Le Van Nam")
print("MSSV: 235752021610085")
print("################################")
#########################################

input_string=input("nhap mot cau: ")
uppercase=0
lowercase=0
for char in input_string:
    if char.isupper():
        uppercase += 1
    elif char.islower():
        lowercase += 1
        print(f"so chu hoa:{uppercase}")
        print(f"so chu thuong:{lowercase}")
