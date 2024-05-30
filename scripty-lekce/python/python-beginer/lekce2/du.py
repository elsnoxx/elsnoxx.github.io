import turtle
import time


window = turtle.Screen()
turtle = turtle.Turtle()



#  pismeno R
def pismeno_R():
    turtle.color("green")
    turtle.penup()
    turtle.forward(50)
    turtle.left(90)
    turtle.forward(100)
    turtle.right(90)
    turtle.pendown()
    turtle.left(90)
    turtle.forward(100)
    turtle.right(90)
    turtle.circle(-50, 180)
    turtle.left(90)
    turtle.forward(100)
    turtle.penup()
    turtle.left(180)
    turtle.forward(100)
    turtle.pendown()
    turtle.right(160)
    turtle.forward(105)
    turtle.penup()
    turtle.left(70)
    turtle.forward(50)
    turtle.pendown()


# Pismeno I
def pismeno_I():
    turtle.color("pink")
    turtle.left(90)
    turtle.forward(200)

#  Pismeno C
def pismeno_C():
    turtle.color("yellow")
    turtle.penup()
    turtle.right(90)
    turtle.forward(130)
    turtle.right(180)
    turtle.pendown()
    turtle.circle(100, 180)
    turtle.penup()
    turtle.forward(70)
    turtle.pendown()

#  Pismeno H
def pismeno_H():
    turtle.color("blue") 
    turtle.left(90)
    turtle.forward(200)
    turtle.left(180)
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(50)
    turtle.left(90)
    turtle.forward(100)
    turtle.left(180)
    turtle.forward(200)
    turtle.left(90)

#  pismeno A
def pismeno_A():
    turtle.color("purple")
    turtle.penup()
    turtle.forward(50)
    turtle.pendown()
    turtle.penup()
    turtle.forward(20)
    turtle.pendown()
    turtle.left(70)
    turtle.forward(200)
    turtle.right(140)
    turtle.forward(200)
    turtle.back(100)
    turtle.right(110)
    turtle.forward(70)
    turtle.penup()
    turtle.left(90)
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(100)



#  pismeno D
def pismeno_D():
    turtle.color("red")
    turtle.penup()
    turtle.forward(50)
    turtle.left(90)
    turtle.forward(100)
    turtle.right(90)
    turtle.pendown()
    turtle.left(90)
    turtle.forward(100)
    turtle.right(90)
    turtle.circle(-100, 180)
    turtle.right(90)
    turtle.forward(100)
    
#  pismeno F
def pismeno_F():
    turtle.color("black")
    turtle.left(90)
    turtle.forward(200)
    turtle.right(90)
    turtle.forward(100)
    turtle.back(100)
    turtle.right(90)
    turtle.forward(80)
    turtle.left(90)
    turtle.forward(50)
    turtle.back(50)
    turtle.right(90)
    turtle.forward(120)

    turtle.penup()
    turtle.left(90)
    turtle.forward(140)
    turtle.pendown()
    
    pass
#  pismeno E
def pismeno_E():
    turtle.color("black")
    turtle.left(90)
    turtle.forward(200)
    turtle.right(90)
    turtle.forward(100)
    turtle.back(100)
    turtle.right(90)
    turtle.forward(80)
    turtle.left(90)
    turtle.forward(50)
    turtle.back(50)
    turtle.right(90)
    turtle.forward(120)
    turtle.left(90)
    turtle.forward(90)


    turtle.penup()
    turtle.forward(60)
    turtle.pendown()
    pass
#  pismeno K
def pismeno_K():
    turtle.color("pink")
    turtle.left(90)
    turtle.forward(200)
    turtle.back(100)

    turtle.right(40)
    turtle.forward(130)
    turtle.back(130)
    turtle.left(60)

    turtle.right(160)
    turtle.forward(130)

    turtle.penup()
    turtle.left(50)
    turtle.forward(50)
    turtle.pendown()


    pass

while True:
    turtle.shape("turtle")
    turtle.speed(200)
    turtle.pensize(2)

    turtle.penup()
    turtle.left(180)
    turtle.forward(350)
    turtle.left(180)
    turtle.pendown()

    pismeno_R()
    pismeno_I()
    pismeno_C()
    pismeno_H()
    pismeno_A()
    pismeno_R()
    pismeno_D()

    turtle.penup()
    turtle.left(90)
    turtle.forward(550)
    turtle.left(90)
    turtle.forward(400)
    turtle.left(90)
    turtle.pendown()

    pismeno_F()
    pismeno_I()
    pismeno_C()
    pismeno_E()
    pismeno_K()

    time.sleep(2)
    turtle.clear()
    turtle.reset()
    

window.exitonclick()