#dado el siguien te vector
numeros=[4,98,257,-85,0,21,-582,184,-293]
#lo ordeno por comodidad
numeros.sort()
#variable para la suma inicada en 0
resSuma=int(0)
#lista vacia para positivos.
positivos=[]
#lista vacia para pares.
pares=[]
#informar el Mayor, la suma, cantidad de positivos, crea una lista con numeros pares.
#la suma
for numero in numeros:
    resSuma+=numero
#cantidad de positivos
for numero in numeros:
    if numero>0:
        positivos.append(numero)
#cantidad de pares
for numero in numeros:
    if numero%2==0:
        pares.append(numero)
pares.remove(0)

while True:

    print("---Menu---")
    print("1 - Mostrar lista.")
    print("2 - Mostrar el mayor.")
    print("3 - Mostrar la suma.")
    print("4 - Mostrar cantidad de positivos.")
    print("5 - Mostrar numeros pares.")
    print("6 - Salir")

    opcion=input("ingrese número de opcion : ")

    if opcion=="1":
        print(f"los numeros son: {numeros}")

    elif opcion=="2":
        print(f"El mayor es : {numeros[(len(numeros)-1)]}")

    elif opcion=="3":
        print(f"La suma de los números es : {resSuma}")
        
    elif opcion=="4":
        print(f"Hay {len(positivos)} positivos en la lista")

    elif opcion=="5":
        print(f"Los números pares de la lista son {pares}")

    elif opcion=="6":
        break

    else:
        print("Opcion no valida")