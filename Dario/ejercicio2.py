#1-Hacer una función llamada doble, que devuelva el doble de un número.
def doble(a):
    numdoble = a*2
    return numdoble
#llamando a la funcion
num1 = float(input("ingrese un numero : "))
print(doble(num1))


#2-Hacer una funcion saludo, que pregunte el nombre al usuario, 
# luego lo salude diciendo "Encantado de conocerte Fulano", donde Fulano sera el nombre que haya 
# contestado el usuario. por ultimo la funcion debe devolver el nombre del usuario.
def saludo():#no se llama a un parametro, solo se define la funcion.
    nom=input("Ingrese su nombre : ")#se crea la variable y se pregunta
    print("Encantado de conocerte,",nom+"!")#se toma la variable y se imprime un saludo cordial.
    return nom#retorna la variable

#3-Hacer una funcion que pregunte la edad al usuario: "cuantos años tenes Fulano?"
#  donde Fulano sera el nombre que haya recibido como parámetro. 
# La función debe retornar la edad.
def edad(nombre):#se crea una funcion llamando a un parametro
    edad=input("Cuantos años ténes " + nombre + "? ")#se crea una variable y se guarda 
    return edad#retorna la variable

#llamando a las 2 anteriores funciones
nombre=saludo()
print(edad(nombre))


#4-Hacer una función, que retorne el producto entre 3 números.
def multriple(num1,num2,num3):
    return print(num1*num2*num3)
#llamando a la funcion
num1=float(input("ingrese primer número : "))
num2=float(input("ingrese segundo número : "))
num3=float(input("ingrese tercer número : "))
print(multriple(num1,num2,num3))

#5-Hacer una función que sirva para calcular el iva de un producto.
def calcIva(a):
    iva=a*.21
    return iva
#llamando a la funcion

precio=float(input("ingrese precio : "))
print(calcIva(precio))