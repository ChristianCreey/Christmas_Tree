import turtle
turtle.speed(2)

#helmet outline setup
turtle.penup()
turtle.goto(-170,-130)
turtle.pendown()

turtle.pensize(10)
turtle.pencolor("gray")
turtle.fillcolor("black")
#helmet outline
turtle.begin_fill()
turtle.goto(-120,-10)
turtle.goto(-80,80)
turtle.goto(-70,110)
turtle.goto(-10,130)
turtle.goto(60,100)
turtle.goto(100,50)
turtle.goto(100,-40)
turtle.goto(130,-150)
turtle.goto(-50,-150)
turtle.goto(-170,-130)
turtle.end_fill()

#left eye setup
turtle.penup()
turtle.goto(-40,-60)
turtle.pendown()

turtle.pensize(3)
turtle.pencolor("white")
turtle.fillcolor("gray")

#left eye
turtle.begin_fill()
turtle.circle(25)
turtle.end_fill()

#right eye setup
turtle.penup()
turtle.goto(40,-60)
turtle.pendown()

turtle.pensize(3)
turtle.pencolor("white")
turtle.fillcolor("gray")

#right eye
turtle.begin_fill()
turtle.circle(25)
turtle.end_fill()

#helmet lines setup
turtle.penup()
turtle.goto(-170,-130)
turtle.pendown()

turtle.pensize(8)
turtle.pencolor("gray")

#helmet lines
turtle.goto(-100,-120)
turtle.goto(-90,-30)
turtle.goto(-40,0)
turtle.goto(70,-10)
turtle.goto(100,-40)

#mouth area setup
turtle.penup()
turtle.goto(-50,-150)
turtle.pendown()

turtle.color("gray")
turtle.fillcolor("white")

#mouth area
turtle.begin_fill()
turtle.goto(-10,-100)
turtle.goto(10,-100)
turtle.goto(50,-150)
turtle.goto(-50,-150)
turtle.end_fill()

#main title setup
turtle.penup()
turtle.goto(-100,-180)
turtle.color("black")


#main title
turtle.write("Darth Vader",font=("Arial",20))

#subtitle setup
turtle.penup()
turtle.goto(-100,-195)
turtle.color("gray")

#subtitle
turtle.write("100 lines of code",font=("Arial",15))