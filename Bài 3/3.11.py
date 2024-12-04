print("Sinh vien: Le Van Nam")
print("MSSV: 235752021610085")
print("################################")
#########################################

def benefit(t, n, k):
    A = n * (1 + t / 100) ** k
    return A
t = float(input("Nhập lãi suất hàng tháng (t%): "))
n = float(input("Nhập số vốn ban đầu (n): "))
k = int(input("Nhập số tháng gửi (k): "))
result = benefit(t, n, k)
print(f"Số tiền nhận được sau {k} tháng là: {result:.2f}")

    
