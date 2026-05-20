#1-Preguntarle números al usuario mientras no ingrese 0. 
# Luego informar la cantidad de números ingresados.

#num=input("ingrese un número. 0 termina el programa. ")
#print(num)

#while num!=0:
#    num=int(input("ingrese un número. 0 termina el programa. "))

#2-Preguntarle números al usuario mientras no ingrese 0.
# Luego informar la suma de los números ingresados

num=float(input("ingrese un número. 0 termina el programa. "))
cont=float(0)
sum=float(0)
#mayor=float(0)
print(num)
if num!=0:
    mayor=num
    while num!=0:
        cont=cont+1
        sum=sum+num
        if mayor<num:
            mayor=num
        num=int(input("ingrese un número. 0 termina el programa. "))
    prom=sum/cont
    print("ingreso ", cont , "números")
    print("La suma de los números es : ", sum)
    print("El promedio es : ",prom)
    print("El mayor es : ",mayor)
else:
    print("no ingreso numero")

