#crear un programa tipo calculadora que se pueda sumar, restar, dividir y multiplicar, 
# recordando que dividir para 0 no es posible. (Debe aparecer que no se puede dividir para cero) 
# Desarrollar en Python el programa, el programa debe pedir el nombre del
# Usuario, apellido, edad, cédula y ciudadanía y al presentar el resultado aparezca :
# “ Buenos días, USUARIO con cédula TAL, edad X, y ciudadanía X el resultado es: RESULTADO”. 
# Pueden usar if y while(Investigacion) 

a=0; b=0; resultado=0.0
nombre=""; apellido=""; cedula="" 
ciudadania=""; operacion=""
opcion=0; edad=0
repetirBool=True 
repetir=0

print("INICIO DE SESION")
print("Ingreso de datos")
nombre=input("Nombre: ")
apellido=input("Apellido: ")
edad=input("Edad: ")
cedula=input("Cedula: ")
ciudadania=input("Ciudadania: ")
while(repetirBool):
    print("***Calculadora***")
    opcionn=int(input("1. Suma\n2. Resta\n3. Multiplicacion\n4. Division\nOpcion: "))
    if(opcionn==1):
        operacion="Suma"
        a=int(input("Ingrese primer numero: "))
        b=int(input("Ingrese segundo numero: "))
        resultado=a+b

    if(opcionn==2):
        operacion="Resta"
        a=int(input("Ingrese primer numero: "))
        b=int(input("Ingrese segundo numero: "))
        resultado=a-b

    if(opcionn==3):
        operacion="Multiplicacion"
        a=int(input("Ingrese primer numero: "))
        b=int(input("Ingrese segundo numero: "))
        resultado=a*b
        
    if(opcionn==4):
        cero=True
        operacion="Division"
        a=int(input("Ingrese primer numero: "))
        while(cero):
            b=int(input("Ingrese segundo numero: "))
            if(b==0):
                print("Error!, no se puede dividir para 0...")
                cero=True
            else:
                cero=False
        resultado=a/b

    print("Buenos días ",nombre," con cedula ",cedula," y  ciudadania ",ciudadania," el resultado de la",operacion," es: ",resultado)
    repetir=int(input("Desea volver a calcular?\n1. SI\n2. NO\nOpcion: "))
    if(repetir==1):
        repetirBool=True
    elif(repetir==2):
        print("Cerrando calculadora...")
        break