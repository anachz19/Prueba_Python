print("Escoja la accion a realizar")
print("""
0.- Comparar numeros
1.- Suma
2.-Resta
3.- Division
4.- Imprimir su datos
5.- Multiplicacion
6.- Multiplicacion de clase
7.- Salir
""" )
var= int(input())

if var==0:
    numero= int(input("Ingrese un numero "))
    b= int(input("Ingrese otro numero "))

    if numero<b:
        print("El numero a es menor que b y son diferentes")
    else:
        print("El numero a es mayor que b y son diferentes")
        if numero==b:
            print("Tus numeros son iguales")

if var==1:
    numero1= int(input("Ingrese un numero "))
    numero2= int(input("Ingrese otro numero "))
    Resultado= numero1+numero2
    print("La suma de sus 2 numeros son: ", Resultado )

if var==2:
    numero1= int(input("Ingrese un numero "))
    numero2= int(input("Ingrese otro numero "))
    Resultado= numero1-numero2
    print("La resta de sus 2 numeros son: ", Resultado )

if var==3:
    numero1= int(input("Ingrese un numero "))
    numero2= int(input("Ingrese otro numero "))
    Resultado= numero1/numero2
    print("La division de sus 2 numeros son: ", Resultado )
if var==4:
    nombre= input("Ingrese su nombre")
    edad= input("Ingrese su edad")
    peso= input("Ingrese su peso")
    print("Su nombre es: ", nombre, "\n", "Su edad es: ", edad, "\n", "Su peso es: ", peso)

if var==5:
    numero1= int(input("Ingrese un numero "))
    numero2= int(input("Ingrese otro numero "))
    Resultado= numero1*numero2
    print("La Multiplicacion de sus 2 numeros son: ", Resultado )

if var==6:
    print("Que tabla quieres?")
    a=int(input())
    var= int(input("Hasta que numero"))
    for var in range(1, var+1):
        print(var, "x= ",a, var*a)

if var==7:
    print("Pulsa enter.")
input(".......")
