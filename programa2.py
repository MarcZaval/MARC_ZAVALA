# Escribir un programa que pida al usuario dos números enteros y muestre por pantalla la <a> entre <b> da un cociente <c> y un resto <r> donde <a> y 
# <b> son los números introducidos por el usuario, y <c> y <r> son el cociente y el resto de la división entera respectivamente.

a = input("Inserte 1er. numero entero: ")
b = input("Inserte 2do. numero entero: ")

print (a + " entre " + b + "," " da Cociente de: " + str(int(a) // int (b)) + " y un resto de: " + str(int(a) % int(b)))



