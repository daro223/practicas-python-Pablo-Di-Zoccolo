
frutas=["manzanas","peras","bananas","duraznos"]
print(frutas[0],frutas[len(frutas)-1])

"""tomando el array del ejercicio 1,
 agregale al final el valor "naranjas" e informar la cantidad de elementos que contiene"""
frutas.append("naranjas")
print(len(frutas))

"""preguntar 20 colores al usuario,
 guardarlos en una lista y luego mostrar los elementos de la lista, uno por renglon."""

colores=[]
for i in range(5):
    colores.append(input("ingrese color : "))

for i in range(5):
    print(colores[i])

"""preguntar 20 colores al usuario, guardarlos en una lista, 
preguntar un color màs y luego informarle si ese color existe en la lista"""

color=input("ingrese un color : ")

for i in range(5):
    if color==colores[i]:
        check=0
        print("este color esta en la lista en la posicion",i)
    if check==1:
        print("este color no esta la lista.")

        respuesta=input("Desea agregarlo? (si o no)")
    
if respuesta=="si":
    colores.append(color)
        


    print(colores)