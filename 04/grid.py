import turtle
count = 0

while (count < 6):
    turtle.penup()
    turtle.goto(-250, -250 + count * 100)
    turtle.pendown()
    turtle.forward(500)
    turtle.penup()
    turtle.left(90)
    turtle.goto(-250 + count * 100, -250)
    turtle.pendown()
    turtle.forward(500)
    turtle.right(90)
    count = count + 1

turtle.exitonclick()
