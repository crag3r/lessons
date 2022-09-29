import turtle
import random

s = turtle.Screen()

obstacle1 = turtle.Turtle()
obstacle1.penup()
obstacle1.shape("square")
obstacle1.goto(random.randint(-300,300), random.randint(-300,300))

obstacle2 = turtle.Turtle()
obstacle2.penup()
obstacle2.shape("square")
obstacle2.goto(random.randint(-300,300), random.randint(-300,300))

obstacle1.onclick(lambda x,y: (obstacle1.hideturtle(), obstacle1.goto(58008, 58008)))
obstacle2.onclick(lambda x,y: (obstacle2.hideturtle(), obstacle2.goto(58008, 58008)))

tutel = turtle.Turtle()
tutel.shape("turtle")
tutel.penup()

def colide(tut, obs):
    return abs(tut.xcor() - obs.xcor()) < 24 and abs(tut.ycor() - obs.ycor()) < 24

def mright():
    if colide(tutel, obstacle1) == True or colide(tutel,obstacle2) == True:
        tutel.reset()
        tutel.penup()
    tutel.setx(tutel.xcor()+15)

def mleft():
    if colide(tutel, obstacle1) == True or colide(tutel,obstacle2) == True:
        tutel.reset()
        tutel.penup()
    tutel.setx(tutel.xcor()-15)

def mdown():
    if colide(tutel, obstacle1) == True or colide(tutel,obstacle2) == True:
        tutel.reset()
        tutel.penup()
    tutel.sety(tutel.ycor()-15)

def mup():
    if colide(tutel, obstacle1) == True or colide(tutel,obstacle2) == True:
        tutel.reset()
        tutel.penup()
    tutel.sety(tutel.ycor()+15)

s.listen()

s.onkeypress(mright, "Right")
s.onkeypress(mleft, "Left")
s.onkeypress(mup, "Up")
s.onkeypress(mdown, "Down")



s.mainloop()
