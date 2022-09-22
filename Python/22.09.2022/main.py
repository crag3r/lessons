import turtle
import random

s = turtle.Screen()

def mright():
    tutel.fd(15)

def mleft():
    tutel.back(15)

def mdown():
    

def mup():


obstacle1 = turtle.Turtle()
obstacle1.penup()
obstacle1.shape("square")
obstacle1.goto(random.randint(-300,300), random.randint(-300,300))

obstacle2 = turtle.Turtle()
obstacle2.penup()
obstacle2.shape("square")
obstacle2.goto(random.randint(-300,300), random.randint(-300,300))

tutel = turtle.Turtle()
tutel.shape("turtle")

turtle.listen()

s.onkeypress(mright, "Right")
s.onkeypress(mleft, "Left")
s.onkeypress(mup, "Up")
s.onkeypress(mdown, "Down")



turtle.exitonclick()

