import turtle

s = turtle.Screen()
t = turtle.Turtle()

t.hideturtle()
t.speed(5)
s.bgcolor("black")
s.title("FELIZ NAVIDAD")
s.setup(1500,800)
#s.screensize(800,800)

t.shape("triangle")
t.color("green")
t.fillcolor("green")
t.begin_fill()
t.pensize(3)
t.forward(200)
t.left(140)
t.forward(100)
t.right(140)
t.forward(50)
t.left(140)
t.forward(100)
t.left(220)
t.forward(50)
t.left(140)
t.forward(100)
t.left(220)
t.forward(50)
t.left(140)
t.forward(100)

#inverso
t.left(80)
t.forward(100)
t.left(140)
t.forward(50)
t.left(220)
t.forward(100)
t.left(140)
t.forward(50)
t.left(220)
t.forward(100)
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
t.pensize(3) #grosor
t.left(270)
t.forward(150)
t.right(90)
t.forward(79)
t.right(90)
t.forward(150)
t.end_fill() #fin relleno


#title
t.penup()
t.left(180)
t.forward(200)
t.color("red","white")
t.write("MERRY CHRISTMAS", font=("Times",25))
t.forward(30)
t.color("red","white")
t.write("and  HAPPY NEW YEAR 2022")
t.forward(30)

#space
t.penup()
t.right(181.5)
t.forward(550)
t.left(273)
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
turtle.done()

#final spin
#turtle.right(1000)
#turtle.exitonclick()