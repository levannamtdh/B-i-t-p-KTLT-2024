print("Sinh vien: Le Van Nam")
print("MSSV: 235752021610085")
print("################################")
#########################################

class StringReverser:
    def __init__(self, input_string):
        self.input_string = input_string  
    
    def reverse_words(self):
        words = self.input_string.split()  
        reversed_words = [word[::-1] for word in words]  
        return ' '.join(reversed_words)  
input_string = input("Nhập một chuỗi: ")  
reverser = StringReverser(input_string)  
result = reverser.reverse_words()  
print(f"Chuỗi sau khi đảo ngược từng từ: {result}")
