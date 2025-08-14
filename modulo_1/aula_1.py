# Listas
    # Declaradas por []
    # São mutáveis
    # Não misturar tipos de variáveis (por exemplo, strings e integer)

lista = [19, 35, 89, 76, 98, 16, 54]
lista_string = ['maçã', 'banana', 'laranja']
lista_vazia = []
lista_aninhada = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# Funções

lista_string.append('melancia') # Adiciona um elemento ao final da lista
print(lista_string)

# lista_string.remove('maçã') # Remove um elemento da lista
# print(lista_string)

# lista_string.clear() # Limpa a lista
# print(lista_string)

print(len(lista)) # Tamanho da lista

print(max(lista)) # Elemento de maior valor da lista

print(min(lista)) # Elemento de menor valor da lista

print(sum(lista)) # Soma dos elementos da lista

# Slicing 
    # Relaciona-se com indexação
    # Chama trechos específicos da lista
    # Permite acessar sub-conjuntos da lista
    # Sintaxe: lista[inicio:fim:pula]
    # O elemento 'fim' não é incluído

print(lista[5]) # Elemento específico da lista

print(lista[::]) # Lista total

print(lista[2:5]) # Começo e fim definidos

print(lista[3:]) # Elementos com ínício no índice 3

print(lista[:4]) # Elementos do início ao índice 3

print(lista[::2]) # Elementos pulando de 2 em 2

print(lista[::3]) # Elementos pulando de 3 em 3

print(lista_string[:2]) # Elementos do início ao índice 1

print(lista_aninhada[:2]) # Elementos do início ao índice 1