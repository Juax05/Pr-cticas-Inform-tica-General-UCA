'''
Desarrollar una función booleana que reciba como parámetro un número entero positivo
y retorne verdadero (True) o falso (False) según sea el número perfecto o no. Luego
utilizarla en un programa que encuentre y muestre por pantalla los primeros cuatro
números perfectos.
Definición: Un número perfecto es un entero positivo, que es igual a la suma de todos
los enteros positivos (excluido él mismo) que son divisores del número. Por ejemplo, el
primer número perfecto es 6, ya que los divisores de 6 son 1, 2, 3 y 1 + 2 + 3 = 6.
'''
def esPerfecto(num):
    perfecto=False
    suma=0
    for n in range(1,num):
        if num%n==0:
            suma+=n
    if suma==num:
        perfecto=True
    return perfecto
    
def main():
    num=int(input("ingrese num "))
    print(esPerfecto(num))
    if esPerfecto(num):
        print("es perfecto")
    else:
        print("no es perfecto")
main()