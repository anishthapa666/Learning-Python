import turtle

def draw_cake():
    turtle.speed(2)
    
    # Draw the base
    turtle.penup()
    turtle.goto(-100, -100)
    turtle.pendown()
    turtle.fillcolor("chocolate")
    turtle.begin_fill()
    for _ in range(2):
        turtle.forward(200)
        turtle.left(90)
        turtle.forward(100)
        turtle.left(90)
    turtle.end_fill()

    # Draw the top layer
    turtle.penup()
    turtle.goto(-80, 0)
    turtle.pendown()
    turtle.fillcolor("pink")
    turtle.begin_fill()
    for _ in range(2):
        turtle.forward(160)
        turtle.left(90)
        turtle.forward(60)
        turtle.left(90)
    turtle.end_fill()

    # Add candles
    for x in range(-70, 90, 30):
        turtle.penup()
        turtle.goto(x, 60)
        turtle.pendown()
        turtle.pensize(5)
        turtle.pencolor("brown")
        turtle.goto(x, 100)

    turtle.done()

draw_cake()
