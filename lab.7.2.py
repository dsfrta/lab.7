def print_hi(name):

    print(f'Hi, {name}')

if __name__ == '__main__':
    print_hi('PyCharm')
from turtle import *
from random import *

R = 2
screen = Screen()
screen.setup(width=1.0, height=0.9)
screen.setworldcoordinates(-3, -3, 3, 3)
screen.bgcolor("white")
screen.tracer(0)
t = Turtle()
t.hideturtle()

t.color("black")
t.pensize(2)

# это справа сверху
t.penup()
t.goto(0, 0)
t.begin_fill()
t.goto(R, 0)
t.setheading(90)
t.circle(R, 90)
t.goto(0, 0)
t.end_fill()

# это слева снизу
t.penup()
t.goto(0, 0)
t.begin_fill()
t.goto(-R, 0)
t.goto(0, -R)
t.goto(0, 0)
t.end_fill()

# это оси x и y
t.color("black")
t.pensize(1)
t.penup();
t.goto(-3, 0);
t.pendown();
t.goto(3, 0)
t.penup();
t.goto(0, -3);
t.pendown();
t.goto(0, 3)

# это R и -R
t.penup()
t.goto(R, -0.3);
t.write("R", font=("Arial", 10))
t.goto(-R, -0.3);
t.write("-R", font=("Arial", 10))
t.goto(0.2, -R);
t.write("-R", font=("Arial", 10))

screen.update()

N = 10000
hits = 0

for i in range(N):

    x = uniform(-R, R)
    y = uniform(-R, R)

    in_circle = (x >= 0 and y >= 0 and (x ** 2 + y ** 2) <= R ** 2)

    in_triangle = (x <= 0 and y <= 0 and y >= -x - R)

    t.penup()
    t.goto(x, y)

    if in_circle or in_triangle:
        hits = hits + 1
        t.color("green")
        t.dot(2)
    else:
        t.color("red")
        t.dot(2)

# площадь мишени
S_total = (2 * R) * (2 * R)

# площадь по монте карло
S_mc = S_total * (hits / N)

# площадь
S_circle = (3.14159 * R ** 2) / 4
S_triangle = (R * R) / 2
S_exact = S_circle + S_triangle

# погрешность
error = abs(S_mc - S_exact) / S_exact * 100

t.penup()
t.goto(-2.8, 2.5)
t.color("black")
t.write(
    f"выстрелов: {N}\nпопаданий: {hits}\nплощадь монте карло: {S_mc:.3f}\nточная площадь: {S_exact:.3f}\nпогрешность: {error:.2f}%",
    font=("Arial", 10, "bold"))

screen.update()
screen.exitonclick()