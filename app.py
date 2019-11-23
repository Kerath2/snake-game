import turtle
import time
import random 

posponer = 0.1
# Instanciamos un objeto de tipo Screen y ejecutamos el metodo Screen para generar una ventana en blanco
wn = turtle.Screen()

# Accedemos a sus metodos y le pasamos parametros
wn.title("Juego")
wn.bgcolor("black")
wn.setup(width = 600, height = 600)  #Redimensionar la pantalla
wn.tracer(0)  #Mejores efectos de animaciones


comida = turtle.Turtle()
comida.speed(0)
comida.shape("square")	
comida.penup()
comida.color("white")
comida.goto(0,0)

cabeza = turtle.Turtle()
cabeza.speed(0)
cabeza.shape("square")	
cabeza.penup()
cabeza.color("Green")
cabeza.goto(0,0)

cabeza.direction = "stop"

def arriba():
	cabeza.direction = "up"
def abajo():
	cabeza.direction = "down"
def izquierda():
	cabeza.direction = "left"
def derecha():
	cabeza.direction = "right"


def mov():
	if cabeza.direction == "up":
		y=cabeza.ycor()
		cabeza.sety(y+20)
	if cabeza.direction == "down":
		y=cabeza.ycor()
		cabeza.sety(y-20)
	if cabeza.direction == "right":
		x=cabeza.xcor()
		cabeza.setx(x+20)		
	if cabeza.direction == "left":
		x=cabeza.xcor()
		cabeza.setx(x-20)	


wn.listen()

wn.onkeypress(arriba,"Up")
wn.onkeypress(abajo,"Down")
wn.onkeypress(izquierda,"Left")
wn.onkeypress(derecha,"Right")


while True:
	wn.update()
	mov()
	time.sleep(posponer)

	if cabeza.distance(comida) < 20:
		x=random.randint(-280,280)
		y=random.randint(-280,280)
		comida.goto(x,y)
