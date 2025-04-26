import turtle


screen = turtle.Screen()
screen.bgcolor("white")


t = turtle.Turtle()
t.pensize(2)

# Draw a square
t.color("blue")
for _ in range(4):
    t.forward(100)
    t.right(90)


t.penup()
t.goto(-50, -50)
t.pendown()


t.color("red")
for _ in range(3):
    t.forward(100)
    t.left(120)


t.hideturtle()
turtle.done()
