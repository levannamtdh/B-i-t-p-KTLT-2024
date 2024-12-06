print("Sinh vien: Le Van Nam")
print("MSSV: 235752021610085")
print("################################")
#########################################

class Hinhchunhat:
    def __init__(self, length, width):
        self.length = length  
        self.width = width    

    def area(self):
        return self.length * self.width

length = float(input("Nhập chiều dài của hình chữ nhật: "))  
width = float(input("Nhập chiều rộng của hình chữ nhật: "))  

hinhchunhat = Hinhchunhat(length, width)

print(f"Diện tích của hình chữ nhật là: {hinhchunhat.area():.2f}")

        
