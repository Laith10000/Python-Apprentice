import turtle
turtle.setup (width=700, height=600)

tina = turtle.Turtle()

tina.hideturtle()

tina.speed(0)

tina.color("silver")

for y in range(4):
    for i in range (5):
        tina.circle(50,steps=4)
        tina.forward(5)
    tina.right(90)
    tina.forward(1)

tina.color("gold")
tina.penup()
tina.goto(0,200)
tina.pendown()

for y in range(4):
    for i in range (5):
        tina.circle(25,steps=4)
        tina.forward(3)
    tina.right(90)
    tina.forward(1)

tina.color("red")
tina.penup()
tina.goto(0,-200)
tina.pendown()

for y in range(4):
    for i in range (5):
        tina.circle(25,steps=4)
        tina.forward(3)
    tina.right(90)
    tina.forward(1)

tina.color("blue")
tina.penup()
tina.goto(200,0)
tina.pendown()

for y in range(4):
    for i in range (5):
        tina.circle(25,steps=4)
        tina.forward(3)
    tina.right(90)
    tina.forward(1)

tina.color("teal")
tina.penup()
tina.goto(-200,0)
tina.pendown()

for y in range(4):
    for i in range (5):
        tina.circle(25,steps=4)
        tina.forward(3)
    tina.right(90)
    tina.forward(1)

tina.color("magenta")
tina.penup()
tina.goto(-200,-200)
tina.pendown()

for y in range(4):
    for i in range (5):
        tina.circle(25,steps=4)
        tina.forward(3)
    tina.right(90)
    tina.forward(1)

tina.color("purple")
tina.penup()
tina.goto(200,200)
tina.pendown()

for y in range(4):
    for i in range (5):
        tina.circle(25,steps=4)
        tina.forward(3)
    tina.right(90)
    tina.forward(1)

tina.color("maroon")
tina.penup()
tina.goto(-200,200)
tina.pendown()

for y in range(4):
    for i in range (5):
        tina.circle(25,steps=4)
        tina.forward(3)
    tina.right(90)
    tina.forward(1)

tina.color("green")
tina.penup()
tina.goto(200,-200)
tina.pendown()

for y in range(4):
    for i in range (5):
        tina.circle(25,steps=4)
        tina.forward(3)
    tina.right(90)
    tina.forward(1)



















































































































































































































































































































































































































turtle.exitonclick()
