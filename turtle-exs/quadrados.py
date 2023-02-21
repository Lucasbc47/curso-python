# Pacote para criar graficos ou desenhos
import turtle

def draw_square(t, tam):
    for i in range(4):
        t.forward(tam)
        t.left(90)
    

dq = turtle.Screen()
dq.bgcolor("red")
jan = turtle.Turtle()

draw_square(jan, 75)
jan.penup()

jan.goto(100, 100)
jan.pendown()
draw_square(jan, 75)
dq.exitonclick()


