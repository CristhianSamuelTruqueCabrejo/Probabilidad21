import time, math

def numeros_generados_semilla():
    semilla = time.time()
    multiplicador  = semilla * 2
    sumando = semilla / 10
    norma = 2**32
    print(semilla)
    numeros_generados = []

    for i in range (10):
        
        semilla = (multiplicador * semilla + sumando) % norma
        numeros_generados.append(semilla)
        
        sumando = multiplicador - int(multiplicador)

    return numeros_generados


numeros_generados = numeros_generados_semilla()
for i,num in enumerate(numeros_generados):
    print(f'{i + 1}. {num}')
