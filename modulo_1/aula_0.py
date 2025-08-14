# Aula 0 - Tempo de execução do código

import time

# Criando uma lista grande
numeros = list(range(10_000_000))

# Opçãos 1: usando for
inicio = time.time()
soma_1 = 0 
soma_2 = 0
for numero in numeros:
    soma_1 += numero
fim = time.time()
print(f"Tempo usando for: {fim - inicio:.2f} segundos")
print(soma_1)

# Opção 2: usando sum()
inicio = time.time()
soma_2 = sum(numeros)
fim = time.time()
print(f"Tempo usando sum: {fim - inicio:.2f} segundos")
print(soma_2)