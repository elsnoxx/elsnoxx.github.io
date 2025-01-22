import turtle

# Nastavení plátna a korytnačky
my_screen = turtle.Screen()
my_screen.setup(600, 600)
my_turtle = turtle.Turtle()
my_turtle.pensize(3)
my_turtle.penup()
my_turtle.goto(-250, -250)
my_turtle.pendown()

# Kresba
for index in range(10):
    my_turtle.forward(500)
    if index % 2 == 0:
        my_turtle.left(90)
        my_turtle.forward(50)
        my_turtle.left(90)
    else:
        my_turtle.right(90)
        my_turtle.forward(50)
        my_turtle.right(90)

turtle.done()