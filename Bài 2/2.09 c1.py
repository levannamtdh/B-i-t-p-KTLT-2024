print("Sinh vien: Le Van Nam")
print("MSSV: 235752021610085")
print("################################")
#########################################

str=input("enter a string:")
dict={}
for n in str:
    keys=dict.keys()
    if n in keys:
        dict[n]+=1
    else:
        dict[n]=1
print(dict)

    
