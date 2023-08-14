import turtle
import random

s = turtle.Screen()
t = turtle.Turtle()

random_colors = ["#0ca90c", "#c20d0d", "#ffffff", "#ffd700", "#3225de", "#8314b9"]

t.hideturtle()
t.speed(5)
s.bgcolor("black")
s.title("FELIZ NAVIDAD")
s.setup(1300,765)
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


# LUCES
maxY = 500
maxX = 500
luces = []

for j in range(0, 10000):
    y = random.randint(-1*maxY, maxY)
    x = random.randint(-1*maxX, maxX)
    luz = turtle.Turtle()
    luz.speed(1000)
    luz.hideturtle()
    luz.penup()
    luz.setpos(x, y)
    luz.pendown()
    luz.dot(random.randint(1, 5), random.choice(random_colors))
    luces.append(luz)
    if len(luces) > 150:
        luzApagar = random.choice(luces)
        luzApagar.clear()



turtle.done()
#turtle.exitonclick()