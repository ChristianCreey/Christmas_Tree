import turtle

#outline of house
turtle.speed(5)
turtle.pensize(20)
#turtle.shape("square")
turtle.color("salmon")

turtle.forward(100)
turtle.left(90)
turtle.forward(100)
turtle.left(50)
turtle.forward(100)
turtle.left(70)
turtle.forward(100)
turtle.right(120)
#
turtle.backward(115)
turtle.right(90)
turtle.forward(100)

#door
turtle.color("red")
turtle.pensize(10)
turtle.left(90)
turtle.forward(50)
turtle.left(90)
turtle.forward(30)
turtle.left(90)
turtle.forward(50)

#space
turtle.penup()
turtle.right(205)
turtle.forward(100)
turtle.pendown()

#windows 1
turtle.color("orange")
turtle.pensize(3)

turtle.right(65)
turtle.forward(20)
turtle.right(90)
turtle.forward(20)
turtle.right(90)
turtle.forward(20)
turtle.right(90)
turtle.forward(20)

turtle.backward(10)
turtle.right(90)
turtle.forward(20)
turtle.backward(10)
turtle.right(90)
turtle.forward(10)
turtle.backward(20)

turtle.penup()
turtle.right(90)
turtle.forward(70)
turtle.pendown()

#windows 2
turtle.color("blue")
turtle.pensize(2)

turtle.right(180)
turtle.forward(20)
turtle.right(90)
turtle.forward(20)
turtle.right(90)
turtle.forward(20)
turtle.right(90)
turtle.forward(20)

turtle.right(90)
turtle.forward(10)
turtle.right(90)
turtle.forward(20)
turtle.backward(10)
turtle.right(90)
turtle.forward(10)
turtle.backward(20)

#title
turtle.penup()
turtle.left(90)
turtle.forward(150)
turtle.color("orange")
turtle.write("cute house", font=("Times",25))
turtle.forward(30)
turtle.color("pink")
turtle.write("In 95 lines of Python code",  font=("Times",15))
turtle.forward(30)
turtle.exitonclick()


#cute house

