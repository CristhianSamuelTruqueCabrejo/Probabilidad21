import time

print('Generador de experimento de Bernoulli')

#-----------------------Ingreso de datos por parte del usuario--------------------
multiplicador  = int(input('Multiplicador: '))
sumando = int(input('Sumando: '))
norma = int(input('Norma: '))
maximo = float(input("Máximo[0,1): "))


semilla = time.perf_counter()
random = 0


i = 0
while i < 10:
    semilla = (multiplicador * semilla + sumando) % norma
    random = semilla / norma

    if random < maximo:    
        print(f"{i+1}.    {1}")
    else: 
        print(f"{i+1}.    {0}")

    i += 1
