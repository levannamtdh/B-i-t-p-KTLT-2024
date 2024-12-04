print("Sinh vien: Le Van Nam")
print("MSSV: 235752021610085")
print("################################")
#########################################

import module
n=int(input("nhap so luong phan tu trong danh sach: "))
lst=[]
for i in range(n):
    value=int(input(f"nhap gia tri cho phan tu{i+1}: "))
    lst.append(value)
lst.sort()
value=int(input("nhap gia tri can tim: "))
found,position=module.binary_search(lst,value)
if found:
    print(f"TRUE")
else:
    print(f"FALSE")
    
