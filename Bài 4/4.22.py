print("Sinh vien: Le Van Nam")
print("MSSV: 235752021610085")
print("################################")
#########################################

def is_all_even_digits(num):
    return all(int(digit)%2==0 for digit in str(num))
even_digit_numbers=[str(num) for num in range(1000,3001) if is_all_even_digits(num)]
print(','.join(even_digit_numbers))
