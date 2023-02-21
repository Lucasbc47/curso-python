# Pacote para criar graficos ou desenhos
import turtle

def draw_squares(t, tam):
    for i in ['red', 'purple', 'hotpink', 'blue']:
        t.color(i)
        t.forward(tam)
        t.left(90)
    

dq = turtle.Screen()
dq.bgcolor("lightgreen")
jan = turtle.Turtle()
jan.pensize(3)


size = 20

for i in range(15):
    draw_squares(jan, size)
    size += 10
    jan.forward(10)
    jan.right(18)

dq.exitonclick()


