#funcion para escribir funciones
def f(valor, expr):
    x = valor
    y = eval(expr)
    return(float(format(y)))

#biseccion
def biseccion():
    expr = input("Introduce la funcion en terminos de x:\n")
    #valores iniciales
    xA = float(input("Introduzca el valor de A:"))
    xB = float(input("Introduzca el valor de B:"))

    errores = []
    raices = []
    i = 0
    
    while(True):
        #Resolver funciones
        fxA = f(xA, expr)
        fxB = f(xB, expr)

        #hallar xR
        xR = (xA + xB)/2
        fxR = f(xR, expr)
        
        #multiplicacion de funciones
        multi = fxA * fxR

        #Almacena raices
        raices.append(xR)

        #Raices
        if (multi > 0):
            xA = xR
        elif(multi < 0):
            xB = xR
        elif(multi == 0):
            break

        #Comprobacion de error
        if(i > 0):
            er = abs(raices[i] - raices[i-1])
            ep = abs((raices[i] - raices[i-1])/raices[i])*100
            errores.append(round(ep, 4))
            if (ep <= 1):
                print(f"El error porcentual es de: {round(ep, 4)}%")
                break
        i += 1

    print("Raices:", raices)
    print("Errores:", errores)
    print("Iteraciones: ", i+1)

# Definiendo el metodo secante
def secant(x0,x1,tol,N):
    print('\n\n ¡METODO SECANTE!')
    step = 1
    condition = True
    
    while condition:
        #resolver funciones
        f0 = f(x0, expr)
        f1 = f(x1, expr)
        
        if f0 == f1:
            print('Error, se divide por 0')
            break

        x2 = x0 - (x1-x0)*f0/(f1 - f0)
        r0 = f(x2, expr)

        if (r0 == 0.0):
            abs(r0)
        print('Iteracion-%d, x2 = %0.3f y f(x2) = %0.3f' % (step, x2, r0))
        x0 = x1
        x1 = x2
        step = step + 1
        
        if step > N:
            print('ya no converge :p')
            break
        
        condition = abs(r0) > tol
    print('\n La raiz es: %0.3f' % x2)

def Secante():
    global expr
    expr = input("Introduce la funcion en terminos de x:\n")
    x0 = float(input('Ingresa el valor de x0: '))
    x1 = float(input('Ingresa el valor de x1: '))
    N = int(input('Ingresa el numero de iteraciones: '))
    # inicializacion del metodo secante
    secant(x0,x1,0.0001, N)


#main
print("Proyecto 2\n\n")
print("Integrantes:\nEllis, Angie\nStanziola, Derek\nGrupo: 1SF131\n\n")

print("Elija un metodo:\n1. Metodo de Biseccion\n2. Metodo Secante\n\n")

p = int(input("Introduzca el valor: "))

if(p == 1):
    biseccion()
elif (p == 2):
    Secante()
else:
    print("Opcion fuera de rango")