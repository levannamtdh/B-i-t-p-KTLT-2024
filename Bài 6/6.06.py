print("Sinh vien: Le Van Nam")
print("MSSV: 235752021610085")
print("################################")
#########################################

class StringHandler:
    def __init__(self):
        self.input_string = ""  

    def get_String(self):
        self.input_string = input("Nhập một chuỗi: ")

    def print_String(self):
        print(self.input_string.upper())

handler = StringHandler()  
handler.get_String()      
handler.print_String()    
