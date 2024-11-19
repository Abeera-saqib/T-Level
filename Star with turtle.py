import turtle
ttl = turtle.Turtle()

#providing the color to be filled
ttl.color("magenta")

#instructing to begin and end and filling the star
ttl.begin_fill()

#for loop to run 5 times to complete drawing a complete star
for j in range(5):
    ttl.forward(200)
    ttl.right(144)
ttl.end_fill()

# hiding the turtle after completing the drawing
ttl.hideturtle()
turtle.done()
