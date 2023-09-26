import math

def f(potencia):  # FUNCIÓN INICIAL DEL PROBLEMA
    k = 0.5  # Constante de proporcionalidad en W/°C
    T0 = 25  # Temperatura ambiente en °C
    temperatura_deseada = 150  # Temperatura deseada en °C
    return k * (temperatura_deseada - T0) - potencia  # Función de temperatura

def df(potencia):  # DERIVADA DE LA FUNCION INICIAL
    return -1  # La derivada de la función es constante (derivada de k*(T-T0) es -k)

def newton_raphson(potencia_inicial, objetivo, max_iter, tolerancia):
    potencia_actual = potencia_inicial

    for n in range(max_iter):
        f_actual = f(potencia_actual)
        derivada_actual = df(potencia_actual)

        if abs(f_actual - objetivo) < tolerancia:
            return potencia_actual  # La solución ha convergido

        potencia_actual = potencia_actual - (f_actual - objetivo) / derivada_actual

    return None  # No se encontró una solución dentro del rango máximo de iteraciones

# PARAMETROS INICIALES
potencia_inicial = 100.0  # Estimación inicial de potencia eléctrica
objetivo = 0  # Diferencia entre la temperatura deseada y la temperatura actual
max_iter = 1000  # Número máximo de iteraciones
tolerancia = 1e-6  # Tolerancia para la precisión

# LLAMADA AL MÉTODO DE NEWTON-RAPHSON
solucion_newton = newton_raphson(potencia_inicial, objetivo, max_iter, tolerancia)

# PRINT DEL RESULTADO
print('\nMétodo de Newton-Raphson:')
if solucion_newton is not None:
    print(f'Potencia eléctrica requerida: {solucion_newton:.6f} vatios')
else:
    print('No se encontró una solución en el número máximo de iteraciones.')