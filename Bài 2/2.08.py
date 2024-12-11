print("Sinh vien: Le Van Nam")
print("MSSV: 235752021610085")
print("################################")
#########################################

def fibonacci_sum():
    a, b = 0, 1
    total = 0  
    
    while b < 4000000:
        if b % 2 == 0:
            total += b
        a, b = b, a + b
    
    print("Tổng các số chẵn trong dãy Fibonacci nhỏ hơn 4 triệu:", total)

fibonacci_sum()


    
