#Desarrollar un programa en el que se ingrese por teclado números enteros hasta que
#se hayan ingresado 5 números pares e informar por pantalla si alguno de ellos es
#también múltiplo de cuatro.

def main():
    i=0
    verdadero=True
    while verdadero:
        while i<5:
            num=int(input("ingrese numero entero: "))
            if (num%2)==0 and (num%4==0):
                i+=1
                print("es par, tambien es multiplo de 4 total de numeros pares: ", i)
            elif  (num%2)==0:
                i+=1
                print("es par, total de numeros pares: ", i)
        res=input("desea continuar? s/n")
        if res=="n":
            verdadero=False
        else:
            verdadero=True
main()

