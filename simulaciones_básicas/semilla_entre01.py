import time

print('Generador de números aleatorios a través del método de semilla')

#-----------------------Ingreso de datos por parte del usuario--------------------
multiplicador  = int(input('Multiplicador: '))
sumando = int(input('Sumando: '))
norma = int(input('Norma: '))


semilla = time.perf_counter()
random  = 0



i = 0
while i < 10:

    semilla = (multiplicador * semilla + sumando) % norma
    random = semilla / norma
    
    print(f"{i+1}.    {random}")

    i += 1
