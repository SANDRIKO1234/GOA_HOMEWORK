from turtle import *

#we want to paint a house

#step 1: draw a square
width(4)
color("purple")
forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)
#end of square

#drawing a door

forward(70)
color("yellow")
left(90)
forward(110)                        #height of the door
right(90)
forward(60)
right(90)
forward(120)


penup()
goto(200, 200)
pendown()
color("red")
begin_fill()
right(150)
forward(200)
left(120)
forward(200) 
end_fill()


penup()
left(45)
forward(30)
left(75)
forward(20)
pendown()
forward(50)
right(90)
forward(50)
right(90)
forward(50)
right(90)
forward(50)
right(90)
penup()
forward(100)
pendown()
forward(50)
right(90)
forward(50)
right(90)
forward(50)
right(90)
forward(50)


exitonclick()


