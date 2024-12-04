print("Sinh vien: Le Van Nam")
print("MSSV: 235752021610085")
print("################################")
#########################################

def get_sum(*num):
    tmp=0
    for i in num:
        tmp+=i
    return tmp
result=get_sum(1,2,3,4,5)
print(result)
