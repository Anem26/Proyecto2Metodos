# Definiendo la función
def f(x):
    
    return x**3 - 2*x - 5

# Definiendo el metodo secante

def secant(x0,x1,tol,N):
    print('\n\n ¡METODO SECANTE!')
    step = 1
    condition = True
    while condition:
        if f(x0) == f(x1):
            print('Error, se divide por 0')
            break
        
        x2 = x0 - (x1-x0)*f(x0)/( f(x1) - f(x0) ) 
        print('Iteracion-%d, x2 = %0.3f y f(x2) = %0.3f' % (step, x2, f(x2)))
        x0 = x1
        x1 = x2
        step = step + 1
        
        if step > N:
            print('ya no converge :p')
            break
        
        condition = abs(f(x2)) > tol
    print('\n La raiz es: %0.3f' % x2)


# seccion para ingresar datos
x0 = float(input('Ingresa el valor de x0: '))
x1 = float(input('Ingresa el valor de x1: '))
N = int(input('Ingresa el numero de iteracinoes: '))
# inicializacion del metodo secante
secant(x0,x1,0.0001, N)