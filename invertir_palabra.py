#developed by: Sebastián D. Arturo - Juan Sebastián Erazo
#ingeniería de sistemas 10 A
#Electiva profesional III - Frameworks

#Vector que almacenará los datos
N=[]
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
    print("[1]: ingresar palabra")
    print("[2]: ingresar palabra")
    print("[3: ingresar palabra")
    x=int(input("digite opcion "))
    if x==1:
        ingresarpantalla()
    elif x==2:
        mostrar()
    elif x==3:
        invertir()
    elif x==4:
        break






