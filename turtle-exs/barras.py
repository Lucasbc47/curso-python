# Pacote para criar graficos ou desenhos
import turtle

def desenhaBarra(t: turtle.Turtle, altura):

	t.begin_fill()
	t.left(90)
	t.forward(altura)
	t.write(altura)
	t.right(90)
	t.forward(40)
	t.right(90)
	t.forward(altura)
	t.left(90)
	t.end_fill()
	
xs = [48,117, 200, 240, 160, 260, 220]
alturamax = max(xs)
numbarras = len(xs)
moldura = 10

tess = turtle.Turtle()
tess.color("blue")
tess.fillcolor("red")
tess.pensize(3)

wn = turtle.Screen()
wn.bgcolor("lightgreen")
wn.setworldcoordinates(
	0-moldura, 0-moldura, 40 * numbarras + moldura,
	alturamax + moldura
)

for a in xs:
	desenhaBarra(tess, a)
wn.exitonclick()