print("Sinh vien: Le Van Nam")
print("MSSV: 235752021610085")
print("################################")
#########################################

def print_pascals_triangle(n):
    for i in range(n):
        row = [1]
        for j in range(1, i):
           row.append(row[j-1] * (i - j) // j)
        if i > 0:
            row.append(1)
        print(*row)
n = int(input("Nhập số n: "))
print_pascals_triangle(n)
        
            
            
        
        
        
        
        
        


