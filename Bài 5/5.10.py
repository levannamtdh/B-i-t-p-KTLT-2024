print("Sinh vien: Le Van Nam")
print("MSSV: 235752021610085")
print("################################")
#########################################


from bubbleSort import bubbleSort
n = int(input("Nhập số lượng phần tử trong danh sách: "))
nlist = []
for i in range(n):
    element = int(input(f"Nhập phần tử thứ {i+1}: "))
    nlist.append(element)
print("Danh sách trước khi sắp xếp:", nlist)
bubbleSort(nlist)
print("Danh sách sau khi sắp xếp:", nlist)
