import math
def f(theta):
    return 10*math.sin(math.radians(theta))-10

def biseccion(a,b,objetivo,max_iter):
    for n in range(max_iter):
        c = (a+b)/2
        f_c = f(c)
        f_a = f(a)
        
        if abs(f_c - objetivo) < 1e-6:
            return c #La solución ha convergido
        
        if (f_a * f_c) < 0:
            b = c
        else:
            a = c
            
    return None # No se encontró la solución dentro del número máximo de iteraciones.


### PARAMETROS INICIALES ###
a = 0
b = 180
objetivo = 12 #distancia objetivo
max_iter = 100 #numero máximo de iteraciones

### LLAMADA AL MÉTODO DE BISECCIÓN ###
solucion_biseccion = biseccion(a,b,objetivo,max_iter)

### PRINT DEL RESULTADO ###
print('Método de Bisección:')
if solucion_biseccion is not None:
    print(f'Ángulo requerido: {solucion_biseccion:.6f} grados')
else:
    print('No se encontró una solución en el número máximo de iteraciones.')
    
    
###### NO ME ARROJO NINGUNA SOLUCION. INTENTE CAMBIAR LAS ITERACIONES Y EL RANGO PERO NO PASO NADA ######

