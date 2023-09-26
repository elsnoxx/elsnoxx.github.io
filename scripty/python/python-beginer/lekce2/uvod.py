import turtle 

window = turtle.Screen()
turtle.Screen().bgcolor("black")
turtle = turtle.Turtle()
turtle.shape("turtle")
turtle.speed(1000)
turtle.pensize(1)


turtle.color("white")

kolo = 20
podvozek = 300
pravU = 90

turtle.right(pravU)
turtle.circle(kolo)
turtle.right(pravU)
turtle.forward(podvozek)
turtle.right(pravU)
turtle.circle(kolo)

turtle.left(pravU)
turtle.penup()
turtle.forward(2 * kolo)
turtle.pendown()

turtle.forward(20)
turtle.right(pravU)
turtle.forward(50)

turtle.right(80)
turtle.forward(50)
turtle.left(60)
turtle.forward(50)

turtle.right(70)
turtle.forward(250)

turtle.right(50)
turtle.forward(60)

turtle.left(50)
turtle.forward(40)
turtle.right(20)
turtle.forward(50)

turtle.right(70)
turtle.forward(40)

turtle.right(90)
turtle.forward(40)

turtle.penup()
turtle.right(90)
turtle.forward(300)



window.exitonclick()