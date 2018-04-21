a= int(input("Ingrese numero 1 "))
b= int(input("Ingrese numero 2 "))
c= int(input("ingrese numero 3 "))

if(a==b and a==c):
    print("Son iguales")
elif a>b and a>c:
    print("El numero 1 es mayor")
elif b>a and b>c:
    print("El numero 2 es mayor")
else:
    print("El numero 3 es mayor")

if a==b and a!=c:
    print("El numero 1 y 2 son iguales pero son diferentes del numero 3")
elif b==c and b!=a:
    print("El numero 2 y 3 son iguales pero son diferentes del numero 1 ")
elif a==C and c!=b:
    print("El numero 1 y 3 son iguales pero son diferentes del numero 2")


input(".....")
