print("Sinh vien: Le Van Nam")
print("MSSV: 235752021610085")
print("################################")
#########################################

import math
a=float(input("nhap a=: "))
b=float(input("nhap b=: "))
c=float(input("nhap c=: "))
if a==0:
    if b !=0:
        x=-c/b
        print("phuong trinh bac nhat voi nghiem: x = {x}")
    else:
        if c==0:
            print("phuong trinh co vo so nghiem")
        else:
            print("phuong trinh vo nghiem")
else:
    delta=b**2-4*a*c
    if delta > 0:
      x1=(-b+math.sqrt(delta))/(2*a)
      x2=(-b-math.sqrt(delta))/(2*a)
      print("phuong trinh co hai nghiem phan biet: x1 = {x1}, x2 = {x2}")
    elif delta == 0:
        x=-b/(2*a)
        print("phuong trinh co nghiem kep: x = {x}")
    else:
        print("phuong trinh vo nghiem")
