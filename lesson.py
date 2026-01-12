import turtle


t = turtle.Turtle()



distance = int(input("Введіть відстань, яку має пройти черепашка: "))


if distance <= 100:
    t.speed(2)     
elif distance <= 300:
    t.speed(5)     
else:
    t.speed(10)    


t.forward(distance)


turtle.exitonclick()

