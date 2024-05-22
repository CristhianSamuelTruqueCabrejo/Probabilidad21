import time

def generador_numeradores_aleatorios():
    multiplicador  = 31
    sumando = 17
    norma = 1351


    semilla = time.perf_counter_ns()
    random  = 0


    semilla = (multiplicador * semilla + sumando) % norma
    random = semilla / norma

    return random

def probabilidad_no_par_correcto(max_ensayos):
    suma = 0

    for i in range(max_ensayos):
        # Inicialización de vectores
        Z = [0] * 8
        D = [0] * 8
        
        # Elección del primer zapato izquierdo y derecho
        Z[0] = int(10 * generador_numeradores_aleatorios()) + 1
        D[0] = int(10 * generador_numeradores_aleatorios()) + 1
        
        # Elección de los demás zapatos izquierdos
        for j in range(1, 8):
            control = True
            while control:
                control = False
                Z[j] = int(10 * generador_numeradores_aleatorios()) + 1
                for r in range(j):
                    if Z[r] == Z[j]:
                        control = True
                        break
        
        # Elección de los demás zapatos derechos
        for j in range(1, 8):
            control = True
            while control:
                control = False
                D[j] = int(10 * generador_numeradores_aleatorios()) + 1
                for r in range(j):
                    if D[r] == D[j]:
                        control = True
                        break
        
        # Comparación de zapatos
        X = 1
        for j in range(8):
            if Z[j] == D[j]:
                X = 0
                break
        
        # Conteo de aciertos
        suma += X

    # Cálculo de la probabilidad
    probabilidad = suma / max_ensayos
    return probabilidad

# Ejemplo de uso
max_ensayos = 10000
prob = probabilidad_no_par_correcto(max_ensayos)
print(f"La probabilidad de no tener algún par correcto es: {prob}")

