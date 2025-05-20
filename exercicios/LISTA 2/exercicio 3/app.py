import turtle

# Classe base Forma
class Forma:
    def desenhar(self):
        print("Desenhando uma forma genérica.")

# Subclasse Círculo
class Circulo(Forma):
    def desenhar(self):
        print("Desenhando um círculo.")
        turtle.penup()
        turtle.goto(0, -50) 
        turtle.pendown()
        turtle.circle(50)  

# Subclasse Quadrado
class Quadrado(Forma):
    def desenhar(self):
        print("Desenhando um quadrado.")
        turtle.penup()
        turtle.goto(-50, 50)  
        turtle.pendown()
        for _ in range(4):
            turtle.forward(100)  
            turtle.right(90)


def main():

    screen = turtle.Screen()
    screen.title("Desenho de Formas com Turtle")


    forma_circulo = Circulo()
    forma_circulo.desenhar()


    forma_quadrado = Quadrado()
    forma_quadrado.desenhar()

 
    turtle.done()

if _name_ == "_main_":
    main()