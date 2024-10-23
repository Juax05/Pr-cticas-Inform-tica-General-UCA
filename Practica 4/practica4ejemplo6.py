"""""
Desarrollar la función aBinario que recibe como parámetro un número decimal (base
10, no mayor a 1000) y retorna el número expresado en binario (base 2). Desarrollar un
programa que ingrese por teclado un entero en base 10, invoque a la función aBinario
y muestre por pantalla el resultado retornado por la función. Ejemplo:
Ingrese un numero decimal: 234
Numero en binario: 11101010
"""""

def aBinario(num):
    binario=""
    while num>0:
        if num%2==0:
            binario+="0"
        elif num%2==1:
            binario+="1"
        num=num//2
    return binario[::-1]

def main():
    print(aBinario(156))
main()