import turtle 

window = turtle.Screen()
turtle = turtle.Turtle()
turtle.shape("turtle")


while True:
    turtle.speed(2)
    turtle.pensize(3)

    # obdelnik
    turtle.forward(150)
    turtle.left(90)
    turtle.forward(75)
    turtle.left(90)
    turtle.forward(150)
    turtle.left(90)
    turtle.forward(75)
    turtle.left(90)

    window.reset()

    turtle.speed(2)
    turtle.pensize(3)


    # 3 kruhy
    turtle.circle(80)
    turtle.penup()
    turtle.forward(80)
    turtle.pendown()    
    turtle.circle(80)
    turtle.penup()
    turtle.forward(80)
    turtle.pendown()    
    turtle.circle(80)
    


    window.reset()


window.exitonclick()