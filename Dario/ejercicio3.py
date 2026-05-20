#1-Preguntarle la edad al usuario e informarle si puede votar o no.

edad=float(input("Decime tu edad"))
if edad >15 and edad <18:
    print("Es optativo votar")
elif edad >17 and edad <=70 :
    print("Es obligatorio votar")
elif edad >0 and edad <17:
    print("No puede votar")
elif edad <1 or edad >150 :
    print("Edad incorrecta")
else :
    print("Número incorrecto")

#2-Pedí al usuario el total de una compra. Si supera $5000, mostrar "Tenés un 10% de descuento".Si no, mostrar "Sin descuento"

totalCompra=float(input("Ingrese total de compra : "))
if totalCompra>=5000 :
    print("Tenes un 10% de decuento.")
else :
    print("Sin descueto")

#La secretaria de un istituto de idioma, tiene que notificar a los alumnos si les corresponde una beca. las becas se otorgan a los promedios de 7 o más. 
#Hacé un algoritmo que la ayude con cada alumno.

def alumno():
    nom=input("Ingrese su nombre : ")
    return nom

def notaProm(nombre):
    nota=float(input("Cúal es la nota promedio de " + nombre + "? "))
    return nota
nombre=alumno()
nota=notaProm(nombre)

if nota >=7 :
    print(nombre,"Tiene beca disponible")
elif nota >=0 :
    print(nombre,"no aplica para la beca")
else :
    print("nota incorrecto")
