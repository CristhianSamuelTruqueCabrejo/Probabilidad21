import time

print('Generador de números aleatorios a través del método de semilla')

#-----------------------Ingreso de datos por parte del usuario--------------------
multiplicador  = int(input('Multiplicador: '))
sumando = int(input('Sumando: '))
norma = int(input('Norma: '))


semilla = time.perf_counter()



i = 0
while i < 10:

    semilla = (multiplicador * semilla + sumando) % norma
     
    
    print(f"{i+1}.    {semilla}")

    i += 1