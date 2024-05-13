from turtle import *
from random import randint
shape("turtle")
colors = ["blue", "red", "orange", "purple"]
shredder = randint(1,10)
user_choose = 0
while user_choose != shredder:
  user_choose = str.lower(input("select direction Left/Right/Direct/Back - "))
  if user_choose == str.lower("left"):
    left(90)
    for color_turtle in colors:
      pensize(randint(1,10))
      color(color_turtle)
      forward(randint(5,30))
    user_choose = randint(1,10)
    if user_choose!= shredder:
      print("Shredder is not here, let's move on")
  elif user_choose == str.lower("right"):
    right(90)
    for color_turtle in colors:
      pensize(randint(1,10))
      color(color_turtle)
      forward(randint(5,30))
    user_choose = randint(1,10)
    if user_choose!= shredder:
      print("Shredder is not here, let's move on")
  elif user_choose == str.lower("direct"):
    for color_turtle in colors:
      pensize(randint(1,10))
      color(color_turtle)
      forward(randint(5,30))
    user_choose = randint(1,10)
    if user_choose!= shredder:
      print("Shredder is not here, let's move on")
  elif user_choose == str.lower("back"):
    left(180)
    for color_turtle in colors:
      pensize(randint(1,10))
      color(color_turtle)
      forward(randint(5,30))
    user_choose = randint(1,10)
    if user_choose!= shredder:
      print("Shredder is not here, let's move on")
print("Shredder here!")