import turtle 

window = turtle.Screen()
turtle = turtle.Turtle()
turtle.shape("turtle")
turtle.speed(10000)
turtle.pensize(1)

for i in range(30):
    turtle.circle(5 * i)
    turtle.circle(-5 * i)
    turtle.left(i)



window.exitonclick()