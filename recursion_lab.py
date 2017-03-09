'''
Using the turtle library, create a fractal pattern.
You may use heading/forward/backward or goto and fill commands to draw
your fractal.  Ideas for your fractal pattern might include
examples from the chapter.  You can find many fractal examples online,
but please make your fractal unique.  Experiment with the variables
to change the appearance and behavior.

Give your fractal a depth of at least 5.  Ensure the fractal is contained on the screen (at whatever size you set it).  Have fun.
(35pts)
'''

import turtle

my_turtle = turtle.Turtle()
my_screen = turtle.Screen()
my_screen.bgcolor('lightblue')

color_list = ["red", "orange", "yellow", "green","blue", "purple", "magenta", "cyan", "black"]

def draw(my_turtle, x, y, heading, dist, depth):
    my_turtle.up()
    my_turtle.goto(x, y)
    my_turtle.color(color_list[depth % (len(color_list[0:2]))])
    my_turtle.down()
    my_turtle.setheading(heading)
    my_turtle.forward(dist)
    new_y = my_turtle.ycor()
    new_x = my_turtle.xcor()

    if depth > 0:
        draw(my_turtle, new_x, new_y, heading + 45, dist/1.5, depth - 1)
        draw(my_turtle, new_x, new_y, heading - 45, dist/1.5, depth - 1)


my_turtle.speed(0)
my_turtle.width(2)

for i in range(0, 360, 90):
    draw(my_turtle, 0, 0, i, 100, 6)


my_screen.exitonclick()