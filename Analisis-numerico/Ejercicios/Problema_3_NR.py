import math

def Hs(H_real):  # FUNCIÓN INICIAL DEL PROBLEMA
    return H_real + 0.2 * math.sin(2 * math.pi * H_real)

def dHs(H_real):  # DERIVADA DE LA FUNCION INICIAL
    return 1 + 0.4 * math.pi * math.cos(2 * math.pi * H_real)

def newton_raphson(H_real_inicial, objetivo, max_iter, tolerancia):
    H_real_actual = H_real_inicial

    for n in range(max_iter):
        H_medida_actual = Hs(H_real_actual)
        derivada_actual = dHs(H_real_actual)

        if abs(H_medida_actual - objetivo) < tolerancia:
            return H_real_actual  # La solución ha convergido

        H_real_actual = H_real_actual - (H_medida_actual - objetivo) / derivada_actual

    return None  # No se encontró una solución dentro del rango máximo de iteraciones

# PARAMETROS INICIALES
H_real_inicial = 9.0  # Estimación inicial de altura real
objetivo = 10.0  # Altura medida deseada en metros
max_iter = 100  # Número máximo de iteraciones
tolerancia = 1e-6  # Tolerancia para la precisión

# LLAMADA AL MÉTODO DE NEWTON-RAPHSON
solucion_newton = newton_raphson(H_real_inicial, objetivo, max_iter, tolerancia)

# PRINT DEL RESULTADO
print('\nMétodo de Newton-Raphson:')
if solucion_newton is not None:
    print(f'Altura real requerida: {solucion_newton:.6f} metros')
else:
    print('No se encontró una solución en el número máximo de iteraciones.')