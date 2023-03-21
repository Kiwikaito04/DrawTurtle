#use turtle libary
import turtle
#set object t for turtle
t=turtle.Turtle()

#resize pen
t.pensize(5)

#set color
t.pencolor("red")
t.fillcolor("blue")

#enable fill color
t.begin_fill()

#draw circle
t.circle(100)

#disable fill color
t.end_fill()

#end
turtle.done()
