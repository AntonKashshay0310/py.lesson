import turtle

t = turtle.Turtle()
t.penup()

t.color("blue")
t.goto(-100, 20)
t.write("Перший текст", font=("Arial", 16, "normal"))

t.color("red")
t.goto(-100, -20)
t.write("Другий текст", font=("Arial", 16, "normal"))








turtle.exitonclick()