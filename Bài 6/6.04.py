print("Sinh vien: Le Van Nam")
print("MSSV: 235752021610085")
print("################################")
#########################################

class RomanConverter:
    def __init__(self):
        self.roman_values = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
    
    def roman_to_int(self, roman):
        total = 0
        length = len(roman)
        
        for i in range(length):
            current_value = self.roman_values[roman[i]]
            if i + 1 < length:
                next_value = self.roman_values[roman[i + 1]]
                if current_value < next_value:
                    total -= current_value
                else:
                    total += current_value
            else:
                total += current_value
        
        return total

converter = RomanConverter()
roman_number = input("Nhập số La Mã: ")
integer_value = converter.roman_to_int(roman_number)
print(f"Số nguyên tương ứng là: {integer_value}")
