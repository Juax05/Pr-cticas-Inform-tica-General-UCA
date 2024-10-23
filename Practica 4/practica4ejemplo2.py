#Desarrollar un programa en el que se ingresen por teclado una cantidad indefinida de
#números enteros positivos hasta que se ingrese 0. A continuación el programa debe
#indicar por pantalla cuál fue el mayor y cuál el menor. Ejemplo:

def main():
    verdadero=True
    while verdadero:
        respuesta=int(input("ingrese cualquier nnumero, si ingresa 0 se termina el programa"))
        if respuesta==0:
            verdadero=False
main()