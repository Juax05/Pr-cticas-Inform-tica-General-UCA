# Desarrollar una función esPrimo que reciba como parámetro un valor numérico y
# determine si dicho número es primo o no, retornando verdadero (True) o falso (False)
# respectivamente. Luego utilizar la función en un programa que solicite al usuario el
# ingreso de una cantidad cant (número natural) y que muestre por pantalla dos listados:
# primero un listado de los números primos comprendidos entre 1 y cant y luego otro
# listado con los primeros cant números primos. Ambos listados se deben imprimir por
# pantalla a 10 columnas, alineando como se muestra en el ejemplo.

def esPrimo(n):
    prim=True
    # Los números menores a 2 no son primos
    if n < 2:
        prim=False
    # Verificamos si el número es divisible por algún número entre 2 y la raíz cuadrada de n
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            prim=False
    return prim

def main():
    cant = int(input("Ingrese una cantidad de números primos: "))
    
    # Primos entre 1 y cant
    print("\nPrimos entre 1 y", cant)
    count = 0
    for i in range(1, cant + 1):
        if esPrimo(i):
            print(f"{i:>5}", end=" ")
            count += 1
            if count % 10 == 0:
                print()
    if count % 10 != 0:
        print()
    
    # Primeros cant números primos
    print("\nPrimeros", cant, "números primos")
    count = 0
    num = 2
    while count < cant:
        if esPrimo(num):
            print(f"{num:>5}", end=" ")
            count += 1
            if count % 10 == 0:
                print()
        num += 1
    if count % 10 != 0:
        print()

main()
