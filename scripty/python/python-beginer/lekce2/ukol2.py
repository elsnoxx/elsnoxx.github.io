import turtle 

window = turtle.Screen()
turtle = turtle.Turtle()
turtle.shape("turtle")
turtle.speed(10)
turtle.pensize(1)

for i in range(360):
    turtle.forward(i)
    turtle.left(59)



window.exitonclick()