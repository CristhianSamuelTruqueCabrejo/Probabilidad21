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

def simular_bernoulli(p, max_iter):
    suma = 0
    for _ in range(max_iter):
        rnd = generador_numeradores_aleatorios()  # Genera un número aleatorio RN D ∈ (0,1)
        if rnd < p:
            suma += 1
    valor_esperado = suma / max_iter
    return valor_esperado

# Parámetros
p = 0.4
max_iter = 10000

# Ejecución del algoritmo
valor_esperado = simular_bernoulli(p, max_iter)
print(f"Valor esperado aproximado: {valor_esperado}")

# Repeticiones para observar la variabilidad
valores_esperados = [simular_bernoulli(p, max_iter) for _ in range(5)]
print(f"Valores esperados en repeticiones: {valores_esperados}")

