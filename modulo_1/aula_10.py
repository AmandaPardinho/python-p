# Bibliotecas
    # Importação de módulos
    # Reutilização de código
    # Funcionalidades adicionais
    # Atalho: ctrl + click : mostra a estrutura da biblioteca

import random # importa a biblioteca
from random import choice # entra na biblioteca e importa o método a ser usado

moeda = choice(["Cara", "Coroa"])
print(moeda)

numero = random.randint(1, 10) # não importou o método, por isso usou o random.
print(numero)

cartas = ["As", "Valete", "Rei", "Rainha"]
random.shuffle(cartas)
print(cartas)

numeros = [1, 2, 3, 4, 5, 6]
numeros_misturados = random.shuffle(numeros)
print(numeros)