print("Sinh vien: Le Van Nam")
print("MSSV: 235752021610085")
print("################################")
#########################################

import turtle
import math

screen = turtle.Screen()
screen.bgcolor("white")
pen = turtle.Turtle()
pen.speed(0)
pen.hideturtle()

def draw_circle(x, y, radius, color):
    pen.penup()
    pen.goto(x, y - radius)  
    pen.pendown()
    pen.color(color)
    pen.circle(radius)

radius = 100  
num_circles = 12  
colors = ['red', 'blue', 'green']  

for i in range(num_circles):
    angle = 2 * math.pi * i / num_circles
    x = radius * math.cos(angle)
    y = radius * math.sin(angle)
    draw_circle(x, y, radius, colors[i % len(colors)])

screen.mainloop()
