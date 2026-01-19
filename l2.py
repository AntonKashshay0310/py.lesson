import turtle

t = turtle.Turtle()

for line in range(8):
    t.forward(100)
    t.backward(100)
    t.right(45)

turtle.exitonclick()