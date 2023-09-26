import math

### DATOS Y DEFINICIONES ###
def potencia_temperatura_deseada(P): 
    k = 0.5 #Constante de proporcionalidad en W/C°
    t_0 = 25 #Temperatura ambiente en C°
    temperatura_deseada = 150 #Temperatura deseada en C°
    
    T = t_0 + (P/k) #Definimos la ecuación para calcular la Temperatura 

    return T - temperatura_deseada #Devolvemos la diferencia entre la temperatura calculada y deseada

### DEFINIMOS FUNCIÓN QUE IMPLEMENTA EL MÉTODO DE BISECCIÓN ###
def metodo_biseccion(func, a, b, tolerancia):
    while (b - a) / 2.0 > tolerancia:
        puntomedio = (a + b) / 2.0
        if func(puntomedio) == 0:
            return puntomedio
        elif func(a) * func(puntomedio) < 0:
            b = puntomedio
        else:
            a = puntomedio
    return (a + b) / 2.0

### LLAMAMOS AL MÉTODO DE BISECCION PARA ENCONTRAR LA POTENCIA ###
potencia_necesaria = metodo_biseccion(potencia_temperatura_deseada, 0, 200, 0.01)

### PRINT DEL RESULTADO ###
print('Potencia eléctrica necesaria para mantenerlo en 150° Celsius:', potencia_necesaria, 'vatios') 

    





