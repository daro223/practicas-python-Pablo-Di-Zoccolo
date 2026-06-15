
frutas=["manzanas","peras","bananas","duraznos"]
print(frutas[0],frutas[len(frutas)-1])

"""tomando el array del ejercicio 1,
 agregale al final el valor "naranjas" e informar la cantidad de elementos que contiene"""
frutas.append("naranjas")
print(len(frutas))

"""preguntar 20 colores al usuario,
 guardarlos en una lista y luego mostrar los elementos de la lista, uno por renglon."""
colores=[]
for i in range(20):
    colores.append(input("ingrese color : "))

"""preguntar un color màs y luego informarle si ese color existe en la lista"""

entrada=input("ingrese un color : ")
#abro un check en False
check=False 
#recorre la Lista de colores, si la entrada coincide con la lista se cambia check se guarda posicion de la Lista y se imprime- 
for color in colores:
    if color == entrada:
        check=True
        posicion = colores.index(color)
        print(f"este color esta en la lista en la posicion {posicion+1}")

#si la entrada no esta en la Lista se informa y se pide una confirmacion para agregarlo al final.
if not check:
    print("este color no esta la lista.")
    respuesta=input("Desea agregarlo en la ultima posicición?  (si o no)")
    if respuesta.lower()=="si":
        colores.append(color)

    print(colores)