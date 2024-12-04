print("Sinh vien: Le Van Nam")
print("MSSV: 235752021610085")
print("################################")
#########################################

input_numbers=input("nhap cac so,phan tach boi dau cach: ").split()
numbers=[int(num) for num in input_numbers]
odd_numbers=[num for num in numbers if num%2!=0]
print("cac so le:",odd_numbers)
