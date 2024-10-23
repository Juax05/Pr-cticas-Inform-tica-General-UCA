"""
La operación factorial de un número entero no negativo n (expresado como n!) es el
producto que resulta de multiplicar n por todos los enteros inferiores a él hasta el uno (0!= 1 por definición). 
Ejemplo:
5! = 5 * 4 * 3 * 2 * 1 = 120
10! = 10 * 9 * 8 * 7 * 6 * 5 * 4 * 3 * 2 * 1 = 3628800
n! = n * (n-1) * (n-2) *...* 3 * 2 * 1 =
………….
Desarrollar un programa que solicite el ingreso de un número entero, verifique si se trata
de un número mayor o igual a 0 y calcule su factorial. 

Para el cálculo del factorial se debe desarrollar una función que reciba como parámetro el número, realice la operatoria
y retorne el resultado. 

En caso de que el usuario ingrese un número negativo, imprimir una advertencia. 

Ejemplos:
Ingrese un número entero: 5
El factorial de 5 es: 120
Ingrese un número entero: -10
No se puede calcular el factorial de un número negativo.
"""

def factorial(num):
    resultado=1
    if num >=0 and num-int(num)==0:
        for n in range(1,num+1):
            resultado*=n
        res="el factorial de {} es {}".format(num,resultado)
    else:
        res="No se puede calcular el factorial de un número negativo."
    return res

def main():
    num=float(input("ingrese num: "))
    print(factorial(num)) 
main()