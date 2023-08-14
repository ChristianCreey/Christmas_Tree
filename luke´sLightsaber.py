import turtle
turtle.speed(2)
turtle.pencolor("silver")
turtle.fillcolor("silver")
turtle.pensize(10)

#middle part
turtle.begin_fill()
turtle.forward(100)
turtle.right(90)
turtle.forward(30)
turtle.right(90)
turtle.forward(100)
turtle.right(90)
turtle.forward(30)
turtle.right(90)
turtle.end_fill()
#space
turtle.penup()
turtle.goto(20,240)
turtle.pendown()

#color and speed
turtle.speed(5)
turtle.pencolor("black")
turtle.fillcolor("lightblue")
turtle.pensize(1)

#top part
turtle.begin_fill()
turtle.forward(60)
turtle.right(90)
turtle.forward(250)
turtle.right(90)
turtle.forward(60)
turtle.right(90)
turtle.forward(250)
turtle.right(90)
turtle.end_fill()

#space
turtle.penup()
turtle.goto(20,-20)
turtle.pendown()

#color and speed
turtle.speed(5)
turtle.pencolor("black")
turtle.fillcolor("silver")
turtle.pensize(10)

#bottom part
turtle.begin_fill()
turtle.forward(60)
turtle.right(90)
turtle.forward(80)
turtle.right(90)
turtle.forward(60)
turtle.right(90)
turtle.forward(80)
turtle.right(90)
turtle.end_fill()

#space
turtle.penup()
turtle.goto(-100,-150)
turtle.pendown()

#title
turtle.write("luke´s lightsaber", font=("Arial",20))


turtle.exitonclick()