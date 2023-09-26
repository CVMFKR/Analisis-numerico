import math

def f(apertura):  # FUNCIÓN INICIAL DEL PROBLEMA
    return 2 * apertura**2 - 3 * apertura + 20 - 30

def df(apertura):  # DERIVADA DE LA FUNCION INICIAL
    return 4 * apertura - 3

def newton_raphson(apertura_inicial, objetivo, max_iter, tolerancia):
    apertura_actual = apertura_inicial

    for n in range(max_iter):
        f_actual = f(apertura_actual)
        derivada_actual = df(apertura_actual)

        if abs(f_actual) < tolerancia:
            return apertura_actual  # La solución ha convergido

        apertura_actual = apertura_actual - f_actual / derivada_actual

    return None  # No se encontró una solución dentro del rango máximo de iteraciones

# PARAMETROS INICIALES
apertura_inicial = 50.0  # Estimación inicial de apertura (50%)
objetivo = 30  # Velocidad de flujo objetivo en litros por minuto
max_iter = 1000  # Número máximo de iteraciones
tolerancia = 1e-6  # Tolerancia para la precisión

# LLAMADA AL MÉTODO DE NR
solucion_newton = newton_raphson(apertura_inicial, objetivo, max_iter, tolerancia)

# PRINT DEL RESULTADO
print('\nMétodo de Newton-Raphson:')
if solucion_newton is not None:
    print(f'Apertura de válvula requerida: {solucion_newton:.6f} %')
else:
    print('No se encontró una solución en el número máximo de iteraciones.')