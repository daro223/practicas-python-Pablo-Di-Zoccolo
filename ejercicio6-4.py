#daro el siguien te vector
numeros=[4,98,257,-85,0,21,-582,184,-293]
numero=float()
#informar el Mayor, la suma, cantidad de positivos, crea una lista con numeros pares.
mayor=float()
sum=float(0)

pares=[]
contador=0
    

while True:

    print("---Menu---")
    print("1 - Mostrar lista.")
    print("2 - Mostrar el mayor.")
    print("3 - Mostrar la suma.")
    print("4 - Mostrar cantidad de positivos.")
    print("5 - Mostrar numeros pares.")
    print("6 - Salir")

    opcion=int(input("ingrese número de opcion : "))

    if opcion==1:
        print(f"los numeros son: {numeros}")

    elif opcion==2:
        for i in range(len(numeros)):
            if mayor>numero:
                mayor=numero
        print=(f"el numero mayor es : {mayor}") 

    elif opcion==3:
        for numero in numeros:
            sum=sum+numero
        print(f"La suma de los números es : {sum}")
        
    elif opcion==4:
        for numero in range(len(numeros)):
            if numero>=0:
                contador+=1
        print(f"Hay {contador} cantidad de positivos en la lista")

    elif opcion==5:
        for i in range(len(numeros)):
            if numero//2:
                pares.append(numero)

    elif opcion==6:
        break