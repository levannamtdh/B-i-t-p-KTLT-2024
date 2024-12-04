print("Sinh vien: Le Van Nam")
print("MSSV: 235752021610085")
print("################################")
#########################################

binary_numbers=input("nhap chuoi cac so nhi phan(phaan tach boi dau phay): ").split(',')
divisible_by_5 = []
for binary in binary_numbers:
    demical_value = int(binary,2)
    if demical_value%5==0:
        divisible_by_5.append(binary)
        print(','.join(divisible_by_5))
