import  turtle

turtle.shape("triangle")
turtle.color("yellow")
turtle.fillcolor("yellow")
turtle.begin_fill()
i = 1
while i <= 5:
    turtle.forward(200)
    turtle.right(144)
    i += 1
turtle.end_fill()