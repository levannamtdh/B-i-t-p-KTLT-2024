print("Sinh vien: Le Van Nam")
print("MSSV: 235752021610085")
print("################################")
#########################################

import my_module
n=int(input("nhap so luong phan tu trong danh sach: "))
lst=[]
for i in range(n):
    value=int(input(f"nhap gia tri cho phan tu{i+1}:"))
    lst.append(value)
sorted_lst=my_module.sort_list(lst)
max_value,max_index=my_module.find_max(lst)
min_value,min_index=my_module.find_min(lst)
print("danh sach sau khi sap xep:",sorted_lst)
print("phan tu lon nhat:",max_value,"vi tri:",max_index)
print("phan tu nho nhat:",min_value,"vi tri:",min_index)
