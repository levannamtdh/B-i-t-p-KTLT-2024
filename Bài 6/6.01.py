print("Sinh vien: Le Van Nam")
print("MSSV: 235752021610085")
print("################################")
#########################################

import math  

class Circle:
    def __init__(self, radius):
        self.radius = radius  

    def area(self):
        return math.pi * self.radius ** 2  

radius = float(input("Nhập bán kính của hình tròn: "))  
circle = Circle(radius)  

print(f"Diện tích của hình tròn là: {circle.area():.2f}")
