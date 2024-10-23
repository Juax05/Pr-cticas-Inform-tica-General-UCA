"""""
Desarrollar un programa que permita ingresar las notas de una cantidad indefinida de
alumnos. 

Considerar notas enteras en el rango de 1 a 10 e ignorar las notas no válidas
(fuera el rango) ingresadas.

La carga finaliza cuando la nota ingresada es 0.

A continuación el programa deberá mostrar la cantidad de alumnos aplazados (nota menor
a 4), la cantidad de alumnos aprobados (nota entre 4 y 7 inclusive) y la cantidad de
alumnos que promocionan la materia (nota superior a 7).
En cada caso, se mostrará el porcentaje del total de notas válidas cargadas que cada caso representa y el promedio
general de todas las notas. 

Ejemplo:
Ingrese nota: 5
Ingrese nota: 4
Ingrese nota: 4
Ingrese nota: 11
Ingrese nota: 2
Ingrese nota: 8
Ingrese nota: 8
Ingrese nota: 2
Ingrese nota: 7
Ingrese nota: 9
Ingrese nota: 0
Cantidad de aplazos: 2 (22.22%)
Cantidad de aprobados: 4 (44.44%)
Cantidad de promocionados: 3 (33.33%)
Promedio general: 5.44
"""
def porcentajes(aplazos,aprobados,promocionados,total_notas,notas):
    promedio_general=notas/total_notas
    print(f"Cantidad de aplazos: {aplazos} ({(aplazos/total_notas)*100})%\nCantidad de aprobados: {aprobados} ({(aprobados/total_notas)*100})%\n Cantidad Promocionados: {promocionados} ({(promocionados/total_notas)*100})%")
    print(f"Promedio General: {promedio_general}")

def cargarNotas():
    r=True
    aplazos=0
    aprobados=0
    promocionados=0
    total_notas=0
    notas=0
    while r==True:
        respuesta=float(input("Ingrese nota: "))
        if (respuesta-int(respuesta))!=0:
            print("numero invalido")
        elif respuesta>10 or respuesta<0:
            print("Fuera de rango")
        elif respuesta>=1 and respuesta<=10: # Si se cumple la condicion
            notas+=respuesta
            total_notas+=1
            if respuesta<4:
                aplazos+=1
            if respuesta>=4 and respuesta<=7:
                aprobados+=1
            if respuesta>7:
                promocionados+=1
        elif respuesta==0: # si la respuesta es cero
            r=False
        else:
            print("numero invalido")
        
    return porcentajes(aplazos,aprobados,promocionados,total_notas,notas)

def main():
    cargarNotas()
main()
