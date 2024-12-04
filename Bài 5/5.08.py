print("Sinh vien: Le Van Nam")
print("MSSV: 235752021610085")
print("################################")
#########################################

import my_modules
n=int(input("nhap so luong phan tu trong danh sach: "))
dist=[]
for i in range(n):
    value=int(input(f"nhap gia tri cho phan tu{i+1}: "))
    dist.append(value)
item=int(input("nhap phan tu can tim: "))
found, position=my_modules.sequential_search(dist,item)
if found:
    print(f"phan tu {item} duoc tim thay tai vi tri {position}.")
else:
    print(f"phan tu {item} khong co trong danh sach.")

