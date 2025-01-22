import turtle

# Načtení souboru
drawing_file = open("scripty-lekce\\python\\python_intermediate\\lekce5\\vstupSamprace.turtledraw", mode="r", encoding="utf-8")
drawing = drawing_file.read().split("|")
drawing_file.close()

# Nastavení plátna
my_screen = turtle.Screen()
my_screen.setup(1000, 1000)
my_turtle = turtle.Turtle()

# Zpracování instrukcí
for instruction in drawing:
  if instruction[0] == "F":
      my_turtle.forward(int(instruction[1:]))
  elif instruction[0] == "B":
      my_turtle.backward(int(instruction[1:]))
  elif instruction[0] == "L":
      my_turtle.left(int(instruction[1:]))
  elif instruction[0] == "R":
      my_turtle.right(int(instruction[1:]))

turtle.done()