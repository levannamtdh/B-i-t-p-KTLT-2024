print("Sinh vien: Le Van Nam")
print("MSSV: 235752021610085")
print("################################")
#########################################

j=[]
for i in range(200,3201):
    if(i%7==0) and (i%5!=0):
        j.append(str(i))
        print(','.join(j))
