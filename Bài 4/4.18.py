print("Sinh vien: Le Van Nam")
print("MSSV: 235752021610085")
print("################################")
#########################################

n=int(input("nhap so nguyen duong n: "))
fibonacci_list=[]
a, b=0, 1
while a<n:
    fibonacci_list.append(a)
    a, b=b, a+b
    print(f"cac so fibonacci nho hon{n} la:")
    print(fibonacci_list)
