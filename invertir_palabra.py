#developed by: Sebastián D. Arturo - Juan Sebastián Erazo
#ingeniería de sistemas 10 A
#Electiva profesional III - Frameworks

#Vector que almacenará los datos
N=[]

#librerias
import os

#Limpiar pantalla
os.system("cls")

def ingresarpantalla():
   

    a = int(input("¿Cuántas letras tiene la palabra que desea ingresar?: "))
    

    for i in range (0,a):
        print("Digite letra ",i+1)
        r = input()
        N.append(r)

def mostrar():
    print ("::: La palabra ingresada es: ")
    for i in range(0,len(N)):
        print ( N[i] )

def invertir():
    print ("::: Mostrar palabra invertida: ")
    for i in range(0,len(N)):
        print ( N[len(N)-i-1] )

while 1==1:
    print("::: MENÚ PRINCIPAL :::")
    print("[1]: Ingresar Palabra")
    print("[2]: Mostrar Palabra")
    print("[3]: Mostrar Palabra (Invertida)")
    print("[4]: Salir")
    x=int(input("Seleccione una opción "))
    if x==1:
        ingresarpantalla()
    elif x==2:
        mostrar()
    elif x==3:
        invertir()
    elif x==4:
        break






