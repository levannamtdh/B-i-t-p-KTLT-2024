print("Sinh vien: Le Van Nam")
print("MSSV: 235752021610085")
print("################################")
#########################################

import math
pos=[0,0]
while True:
    s=input("Nhap huong di chuyen(UP,DOWN,LEFT,RIGHT) va so buoc,hoac nhan enter de ket thuc: ")
    if not s:
        break
    movement = s.split(" ")
    direction = movement[0]
    steps = int(movement[1])
    if direction=="UP":
        pos[1]+=steps
    elif direction=="DOWN":
        pos[1]-=steps
    elif direction=="LEFT":
        pos[0]-=steps
    elif direction=="RIGHT":
        pos[0]+=steps
        distance=math.sqrt(pos[0]**2+pos[1]**2)
        print(f"khoang cach tu vi tri hien tai den vi tri ban dau la:{round(distance)}")
