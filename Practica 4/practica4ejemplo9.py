def nroInvertido(nro):
    num_invertido = 0
    for n in range(len(str(nro))):
        resto = nro % 10
        num_invertido =(num_invertido *10)+resto
        nro=nro//10
    return num_invertido

def esCapicua(nro):
    return nro == nroInvertido(nro)

def main():
    numero = int(input("ingrese el numero: "))
    if (esCapicua(numero)):
        print("el numero es capicua")
    else:
        print("el numero no es capicua")
main()