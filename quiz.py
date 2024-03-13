# Quiz instrucciones condicionales
"""Dados tres números a, b y c, correspondientes a la longitud de los lados de una figura geométrica, determinar si pueden formar los lados de un triángulo."""

# Input
a = float(input("Digite el valor del vertice 1: "))
b = float(input("Digite el valor del vertice 2: "))
c = float(input("Digite el valor del vertice 3: "))

# processing

if a + b > c:
    Resultado = "Se puede utilizar como un triangulo"
    if b + c > a:
        Resultado = "Se puede utilizar como un triangulo"
        if c + a > b:
            Resultado = "Se puede utilizar como un triangulo"
        else:
            Resultado = "No se puede utilizar como un triangulo"

# output 

print("Los lados", a, ",", b, "y", c, Resultado )