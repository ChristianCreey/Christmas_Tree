import turtle
import random

s = turtle.Screen()
t = turtle.Turtle()

c1 = "#0ca90c"
c2 = "#c20d0d"
c3 = "#ffffff"
c4 = "#ffd700"
c5 = "#3225de"
c6 = "#8314b9"

t.hideturtle()
t.speed(5)
s.bgcolor("black")
s.title("FELIZ NAVIDAD")
s.setup(700,700)
t.shape("triangle")
t.color("green")
t.fillcolor("green")
t.begin_fill()
t.pensize(3)
t.forward(200)
for i in range(4):
    t.left(140)
    t.forward(100)
    t.right(140)
    t.forward(50)
t.undo()
t.right(140)
t.forward(100)
for i in range(3):
    t.left(140)
    t.forward(50)
    t.left(220)
    t.forward(100)
t.left(140)
t.forward(195)
t.end_fill()

#tronco
t.shape("square")
t.color("brown")
t.fillcolor("brown")
t.begin_fill()
t.pensize(3)
for i in range(2):
    t.right(90)
    t.forward(150)
    t.right(90)
    t.forward(79)
t.end_fill()

#title
t.penup()
t.right(90)
t.left(-45)
t.forward(300)
t.color("red","white")
t.write("MERRY CHRISTMAS", font=("Times",25))
t.forward(35)
t.color("red","white")
t.write("\tAND", font=("Times",25))
t.forward(35)
t.color("red","white")
t.write("   HAPPY NEW YEAR 2022", font=("Times",25))

#space
t.penup()
t.right(158)
t.forward(590)
t.left(289.5)
t.forward(-30)
t.pendown()

#start
t.pensize(2)
t.shape("triangle")
t.color("yellow")
t.fillcolor("yellow")
t.begin_fill()
i = 1
while i <= 5:
    t.forward(50)
    t.right(144)
    i += 1
t.end_fill()

t.hideturtle()


#Luces

t.penup()
t.shape('circle')
t.color(c1)
t.fillcolor(c1)
t.left(265)
t.forward(260)
t.pendown()
t.circle(5)

t.penup()
t.shape('circle')
t.color(c2)
t.fillcolor(c2)
t.left(90)
t.forward(50)
t.pendown()
t.circle(5)

t.penup()
t.shape('circle')
t.color(c3)
t.fillcolor(c3)
t.left(0)
t.forward(50)
t.pendown()
t.circle(5)

t.penup()
t.shape('circle')
t.color(c4)
t.fillcolor(c4)
t.left(0)
t.forward(50)
t.pendown()
t.circle(5)

t.penup()
t.shape('circle')
t.color(c5)
t.fillcolor(c5)
t.left(0)
t.forward(50)
t.pendown()
t.circle(5)

t.penup()
t.shape('circle')
t.color(c6)
t.fillcolor(c6)
t.left(0)
t.forward(50)
t.pendown()
t.circle(5)




turtle.done()
#turtle.exitonclick()