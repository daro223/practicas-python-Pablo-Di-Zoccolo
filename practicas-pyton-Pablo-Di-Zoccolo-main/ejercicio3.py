#1-Preguntarle la edad al usuario e informarle si puede votar o no.

edad=float(input("Decime tu edad : "))
#si tiene entre 0 y 16 no puede votar
if edad > 0 and edad < 18:
    print("Usted no puede votar.")
#si tiene entre 17 y 70 es obligatorio.
elif edad >= 18 and edad <=70:
    print("Usted vota obligatoriamente.")
#si tiene entre 71 y 150. es optativo votar.
elif edad >70 and edad <150:
    print("Usted puede votar, pero no es obligatorio.")
#si tiene 0 o menos o mas de 150. 
else:
    print(f"La edad '{edad}' no es valida.")

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
