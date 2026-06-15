#dado el siguien te vector
numeros=[4,98,257,-85,0,21,-582,184,-293]

while True:
    #lo ordeno por comodidad.
    numeros.sort()
    #se inicia Lista vacia para guardar los numeros pares.
    pares=[]
    #se inicia Lista vacia para guardar los numeros positivos.
    positivos=[]

    print("---Menu---")
    print("1 - Mostrar lista.")
    print("2 - Agregar número.")
    print("3 - Quitar número.")
    print("4 - Mostrar el mayor.")
    print("5 - Mostrar la suma.")
    print("6 - Mostrar cantidad de positivos.")
    print("7 - Mostrar numeros pares.")
    print("8 - Salir")

    opcion=input("ingrese número de opcion : ")
    #Está opción muestra los elementos de la Lista numeros
    if opcion=="1":
        print(f"los numeros son: {numeros}")
    #Está opcion pide una entrada para guardarlo en la Lista numeros, se imprime-
    elif opcion=="2":
        entrada=float(input("ingrese numero : "))
        numeros.append(entrada)
        print(f"Se agrego '{entrada}' a la lista")
    #Está opcion pide una entrada para eliminar de la Lista numeros- 
    elif opcion=="3":
        borrar=float(input(f"que numero desea quitar de la lista?\n{numeros}\n : "))
        numeros.remove(borrar)
    #Está opcion imprime el número mayor de la Lista numeros-
    elif opcion=="4":
        print(f"El mayor es : {numeros[(len(numeros)-1)]}")
    #Está opción imprime la suma de los números de la Lusta numeros- 
    elif opcion=="5":
        print(f"La suma de los números es : {sum(numeros)}")
    #Está opción recorre la Lista numeros, y guarda los numeros mayores a 0 en la Lista positivos, imprime la cantidad de la Lista positivos-
    elif opcion=="6":
        for numero in numeros:
            if numero > 0:
                positivos.append(numero)
        print(f"Hay {len(positivos)} positivos en la lista")
    #Está opcion recorre la Lista numeros, y si el residuo de la división entre 2 da 0, se guarda en la Lista pares, imprime la Lista Pares-
    elif opcion=="7":
        for numero in numeros: 
            if numero%2==0:
                pares.append(numero)
        print(f"Los números pares de la lista son {pares}")
    #Está opción termina el programa-
    elif opcion=="8":
        break

    else:
        print("Opcion no valida")