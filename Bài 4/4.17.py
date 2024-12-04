print("Sinh vien: Le Van Nam")
print("MSSV: 235752021610085")
print("################################")
#########################################

def tong_ua(x):
    tong = 0
    for i in range(1, int(x**0.5) + 1):
        if x % i == 0:
            tong += i
            if i != x // i:  
                tong += x // i
    return tong

def in_so(n):
    for i in range(1, n):
        if tong_ua(i) > i:
            print(i)

n = int(input("Nhập n: "))
in_so(n)
