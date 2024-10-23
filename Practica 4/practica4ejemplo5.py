""""
Desarrollar una función booleana que reciba como parámetro un número entero de
cuatro cifras y determine si el número cumple la condición de que la suma de las
unidades y las centenas es igual a la suma de las decenas y las unidades de mil. Luego
realizar un programa que encuentre e imprima un listado con todos los números de 4
cifras que cumplan la condición anteriormente citada. Por ejemplo, el número 7821
cumple esta condición ya que 1 + 8 = 2 + 7.
"""

def cumpleCondicion(num):
    res=False
    m=num//1000
    c=(num%1000)//100
    d=(num%100)//10
    u=num%10
    if c+u == d+m:
        res=True
    return res
    
def main():
    num=7821
    print(cumpleCondicion(num))
    print(cumpleCondicion(3421))
main()