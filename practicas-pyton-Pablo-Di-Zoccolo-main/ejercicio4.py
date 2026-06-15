#Repetir 10 veces:
 #  mostrar("Hola")

#for i in range():
#    print("Hola")

#1-Preguntarle el nombre y un numero al usuario.
#Motrar el nombre la cantidad de veces indico.

def pregnombre():
    nom=input("Ingrese su nombre : ")
    return nom

def pregnumero():
    num=int(input("Ingrese un numero : "))
    return num

nom=pregnombre()

for i in range(pregnumero()):
    print(nom)

#2-Mostrar los primeros 25 números naturales.

for i in range(1,26):
    print(i)

#3-Preguntar un número al usuario y mostrar los números naturales hasta dicho número.

nom=pregnombre()
num=pregnumero()
for i in range(1,num+1):
    print(i)

#4-Mostrar la tabla del 2

for i in range(1,11):
    print(f"2 x {i} = {2*i}")
    

#5-Preguntar un número al usuario y mostrar la tabla de ese número.
def tabla(n):
    for i in range(1,11):
        print(f"{n} x {i} = {i*n}")

tabla(pregnumero())
#-extra

for i in range(1,11):
    tabla(i)