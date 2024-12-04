print("Sinh vien: Le Van Nam")
print("MSSV: 235752021610085")
print("################################")
#########################################

input_string=input("nhap mot cau: ")
letters=0
digits=0
for char in input_string:
    if char.isalpha():
        letters += 1
    elif char.isdigit():
        digits += 1
        print(f"so chu cai:{letters}")
        print(f"so chu so:{digits}")
