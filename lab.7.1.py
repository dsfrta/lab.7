def print_hi(name):
    print(f'Hi, {name}')

if __name__ == '__main__':
    print_hi('PyCharm')
import turtle
import math

screen = turtle.Screen()
screen.setup(width=1.0, height=0.9)
screen.setworldcoordinates(-4, -2, 6, 2)
screen.bgcolor("white")

t = turtle.Turtle()
t.speed(0)
t.pensize(2)

t.color("black")
t.penup()
t.goto(-4, 0)
t.pendown()
t.goto(6, 0)
t.penup()
t.goto(0, -2)
t.pendown()
t.goto(0, 2)

t.color("blue")
t.penup()

x = -3.5
first_point = True

while x <= 5.5:


    if x < -2:
        y = -x - 2
    elif x <= -1:
        y = math.sqrt(1 - (x + 1) ** 2)
    elif x <= 1:
        y = 1
    elif x <= 2:
        y = -2 * x + 3
    else:
        y = -1

    t.goto(x, y)

    if first_point == True:
        t.pendown()
        first_point = False

    x = x + 0.02

screen.exitonclick()