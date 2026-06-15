


# pide un numero, calcula el perimetro y la superficie de un cuadrado y muestra.

#lado=input("Ingrese el lado de un cuadrado. cm)")
#lado=float(lado)
#per1=lado*4
#super1=lado*lado
#print("El perimetro del cuadrado es :" , per1 ,"cm")
#print("La superficie del cuadrado es :" , super1 , "cm") 


# pide un numero, lo convierte a fahrenheit.
#celcius=input("valor en celcius")
#celcius=float(celcius)
#fahrenheit=((celcius*9/5)+32) #utiliza la formula {(celuis * 9 / 5) +32}
#print(celcius,"grados celcius son " , fahrenheit , "en fahrenheit") 

# otra manera de convertir un string a int o float
#numero=int(input("ingrese un numero :"))
#print(numero)

# funcion que suma dos numeros por parametro
def suma(a,b):
    result = a + b
    return result # fin funcion.

# algoritmo que pide dos numeros y luego llama a la funcion suma.
a =float(input("Ingrese un numero"))
b =float(input("ingrese un numero"))
print(suma (a,b))

# funcion que devuelve el doble de un numero
def doble(a):
    result=(a)*2
    return result #fin funcion.

# algoritmo que pide un numero y luego llama a la funcion doblenum.
a = float(input("ingrese un numero"))
print(doble(a))