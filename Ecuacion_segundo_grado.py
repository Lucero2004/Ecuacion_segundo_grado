#Ecuación_grado
#programa para resolver una ecuacion de primer grado
import math

print("ingresa los valores para despejar una ecuacion de primer grado")
print("de la forma ax^2+bx+c: ")

a=int(input("ingrese el valor de a: "))
b=int(input("ingrese el valor de b: "))
c=int(input("ingrese el valor de c: "))


i=b^2
y=a*c
d=(-4*(y))

x1=(-b+-math.sqrt(i-d))/2*a


x2=x1*-1
print("la primera x es igual a: "+str(x1))
print("la segunda x es igual a: "+str(x2))

