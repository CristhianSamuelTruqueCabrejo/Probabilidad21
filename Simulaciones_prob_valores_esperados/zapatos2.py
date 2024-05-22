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
        # Inicialización del vector Z
        Z = [0] * 8
        
        # Elección del primer zapato
        Z[0] = int(20 * generador_numeradores_aleatorios()) + 1
        
        # Elección de los demás zapatos
        for j in range(1, 8):
            control = True
            while control:
                control = False
                Z[j] = int(20 * generador_numeradores_aleatorios()) + 1
                for r in range(j):
                    if Z[r] == Z[j]:
                        control = True
                        break
        
        # Comparación de los zapatos extraídos
        M = 0  # contador de pares encontrados
        X = 0  # indicador de par correcto
        
        for j in range(8):
            if Z[j] % 2 == 1:  # si es zapato izquierdo (número impar)
                for q in range(8):
                    if Z[q] == Z[j] + 1:  # si hay zapato derecho correspondiente
                        X += 1
                        break
            if X > 0:
                M = 1
                break
        
        suma += M
    
    # Cálculo de la probabilidad
    probabilidad = 1 - (suma / max_ensayos)
    return probabilidad

# Ejemplo de uso
max_ensayos = 10000
prob = probabilidad_no_par_correcto(max_ensayos)
print(f"La probabilidad de no tener algún par correcto es: {prob:.4f}")
