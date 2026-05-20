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

for i in range(1,26,1):
    print(i)

#3-Preguntar uyn número al usuario y mostrar los números naturales hasta dicho número.

nom=pregnombre()
num=pregnumero()
for i in range(num):
    print(i+1)

#4-Mostrar la tabla del 2

for i in range(1,11,1):
    result = 2*i
    print("2 *",i,"=",result)
    

#5-Preguntar un número al usuario y mostrar la tabla de ese número.
def tabla(n):
    for i in range(1,11,1):
        result = n*i
        print( n,"*",i,"=",result)


#-extra
tabla(pregnumero())


for n in range(1,11):
    for i in range(1,11):
        result = n*i
        print( n,"*",i,"=",result)
