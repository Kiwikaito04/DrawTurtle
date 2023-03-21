#use turtle libary
import turtle
#set object t for turtle
t=turtle.Turtle()

#move the turtle
t.pencolor("white")
t.fillcolor("white")
t.goto(-40,120)

#resize pen
t.pensize(5)

#set color
t.pencolor("blue")
t.fillcolor("red")

#enable fill color
t.begin_fill()

#draw circle
t.circle(150)

#disable fill color
t.end_fill()

#end
turtle.done()
