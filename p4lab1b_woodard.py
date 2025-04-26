import turtle


screen = turtle.Screen()
screen.bgcolor("white")


t = turtle.Turtle()
t.pensize(5)
t.color("blue")


def draw_B():
    t.penup()
    t.goto(-150, 0)
    t.setheading(90)
    t.pendown()
    t.forward(100)  

   
    t.right(90)
    t.circle(-25, 180)

    
    t.left(180)
    t.circle(-25, 180)
    

def draw_W():
    t.penup()
    t.goto(0, 100)
    t.setheading(270)
    t.pendown()
    t.forward(100)
    t.left(135)
    t.forward(50)
    t.right(90)
    t.forward(50)
    t.left(135)
    t.forward(100)


draw_B()
draw_W()


t.hideturtle()
turtle.done()
