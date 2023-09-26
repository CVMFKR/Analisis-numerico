import math

def Hs(H_real):  # FUNCIÓN INICIAL DEL PROBLEMA
    return H_real + 0.2 * math.sin(2 * math.pi * H_real)

def punto_fijo(g, H_real_inicial, objetivo, max_iter, tolerancia):
    H_real_actual = H_real_inicial

    for n in range(max_iter):
        H_medida_actual = g(H_real_actual)

        if abs(H_medida_actual - objetivo) < tolerancia:
            return H_real_actual  # La solución ha convergido

        H_real_actual = H_medida_actual

    return None  # No se encontró una solución dentro del rango máximo de iteraciones

# PARAMETROS INICIALES
H_real_inicial = 7.0  # Estimación inicial de altura real (puedes ajustarla)
objetivo = 10.0  # Altura medida deseada en metros
max_iter = 100  # Número máximo de iteraciones (aumentado)
tolerancia = 1e-3  # Tolerancia para la precisión (reducida)

# LLAMADA AL MÉTODO DEL PUNTO FIJO
solucion_punto_fijo = punto_fijo(Hs, H_real_inicial, objetivo, max_iter, tolerancia)

# PRINT DEL RESULTADO
print('\nMétodo del Punto Fijo:')
if solucion_punto_fijo is not None:
    print(f'Altura real requerida: {solucion_punto_fijo:.6f} metros')
else:
    print('No se encontró una solución en el número máximo de iteraciones.')