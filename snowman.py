import turtle

#title
turtle.penup()
turtle.goto(-75,150)
turtle.write("Snowman", font=("Times", 40))
turtle.goto(-75,130)
turtle.write("46 lines of code", font=("Times",15))

#circle 1
turtle.goto(0,50)
turtle.pendown()
turtle.color("lightblue")
turtle.begin_fill()
turtle.circle(30)
turtle.end_fill()

#circle 2
turtle.penup()
turtle.right(170)
turtle.forward(10)
turtle.pendown()
turtle.color("lightgreen")
turtle.begin_fill()
turtle.circle(45)
turtle.end_fill()

#circle 3
turtle.penup()
turtle.left(60)
turtle.forward(130)
turtle.pendown()
turtle.color("pink")
turtle.begin_fill()
turtle.circle(60)
turtle.end_fill()

#buttons
turtle.penup()
turtle.color("black")
turtle.goto(0,30)
turtle.dot(15)
turtle.goto(0,10)
turtle.dot(15)
turtle.goto(0,-10)
turtle.dot(15)
print("ameliejoliesilvestri")
turtle.exitonclick()