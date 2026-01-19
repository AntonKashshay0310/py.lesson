import turtle

t = turtle.Turtle()

for square in range(5):
    for side in range(4):
        t.forward(30)
        t.right(90)
    t.forward(40)

turtle.exitonclick()



