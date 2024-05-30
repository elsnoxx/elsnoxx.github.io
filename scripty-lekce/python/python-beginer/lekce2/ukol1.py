import turtle 

window = turtle.Screen()
turtle = turtle.Turtle()
turtle.shape("turtle")
turtle.speed(10)
turtle.pensize(3)

while True:
    # obdelnik
    turtle.forward(150)
    turtle.right(90)
    turtle.circle(20)
    turtle.left(180)

    turtle.forward(75)
    turtle.right(180)
    turtle.circle(20)
    turtle.left(270)
    


# turtle.forward(150)
# turtle.right(90)
# turtle.circle(20)
# turtle.left(180)

# turtle.forward(75)
# turtle.right(180)
# turtle.circle(20)
# turtle.left(270)


window.exitonclick()