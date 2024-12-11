print("Sinh vien: Le Van Nam")
print("MSSV: 235752021610085")
print("################################")
#########################################

import turtle
window = turtle.Screen()
window.bgcolor("lightgreen")
painter = turtle.Turtle()
painter.fillcolor('blue')
painter.pencolor('blue')
painter.pensize(3)
def drawsq(t, s):
    for i in range(4):
        t.forward(s)
        t.left(90)
for i in range(1,180):
    painter.left(18)
    drawsq(painter, 200)
