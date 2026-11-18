def print_hi(name):
    print(f'Hi, {name}')
if __name__ == '__main__':
    print_hi('PyCharm')
from turtle import *

screen = Screen()
screen.setup(width=1.0, height=0.9)
screen.setworldcoordinates(0, 0, 4.5, 2.0)
screen.title("график Arcth(x))")
screen.bgcolor("white")

t = Turtle()
t.speed(0)
t.hideturtle()

# оси
t.pencolor("black")
t.penup();
t.goto(0, 0);
t.pendown();
t.goto(4.5, 0);
t.goto(4.4, 0.1);
t.goto(4.5, 0)
t.penup();
t.goto(0, 0);
t.pendown();
t.goto(0, 2.0)
t.penup();
t.goto(4.3, 0.1);
t.write("X", font=("Arial", 12, "bold"))
t.goto(0.1, 1.8);
t.write("Y", font=("Arial", 12, "bold"))

# график
t.pencolor("black")
t.pensize(2)
t.penup()

x = 1.1
first_point = True

while x <= 4.0:
    y = 0
    n = 0
    term = 1 / x

    while abs(term) >= 1e-4:
        y += term
        n += 1
        term = 1 / ((2 * n + 1) * (x ** (2 * n + 1)))

    if first_point:
        t.goto(x, y)
        t.pendown()
        first_point = False
    else:
        t.goto(x, y)

    x = x + 0.05
t.penup()
t.goto(2.25, 1.8)
t.pencolor("black")
t.write("график Arcth(x)", align="center", font=("Arial", 14, "bold"))

screen.exitonclick()
