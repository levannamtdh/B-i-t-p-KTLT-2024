print("Sinh vien: Le Van Nam")
print("MSSV: 235752021610085")
print("################################")
#########################################

import math

def Tinh(R):
    if R <= 0:
        print("Bán kính phải là số dương!")
        return
    chu_vi = 2 * math.pi * R
    dien_tich = math.pi * R * R
    print(f"Chu vi của hình tròn là: {chu_vi:.2f}")
    print(f"Diện tích của hình tròn là: {dien_tich:.2f}")
R = float(input("Nhập bán kính của hình tròn: "))
Tinh(R)
