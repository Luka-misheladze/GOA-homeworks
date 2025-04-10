from turtle import *


#we want to paint a house




#step 1: draw a square




shape("turtle")
width(7)
color("purple")
speed(15)
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
begin_fill()
left(90)
forward(120)
right(90)                                     #height of the door
forward(60)
right(90)
forward(120)
end_fill()


penup()
goto(200, 200)
pendown()

color("blue")
begin_fill()

right(150)
forward(200)                                   #roof of the house
left(120)
forward(200)
end_fill()


penup()
goto(180, 180)
pendown()

end_fill
begin_fill()
right(60)
forward(40)
left(90)
forward(50)                          
left(90)
forward(40)
left(90)
forward(50)                                     #windows of the house
end_fill()

begin_fill()
penup()
goto(60, 180)
pendown()
left(90)
forward(40)
left(90)
forward(50)
left(90)
forward(40)
left(90)
forward(50)
end_fill()



exitonclick()