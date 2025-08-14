# Dicionários
    # Declaradas por {}
    # Estruturas de dados que armazenam pares de chave-valor
    # Permitem acesso rápido aos valores com base em suas chaves
    # Sintaxe: dicionario = {chave1: valor1, chave2: valor2}
    # Acesso aos elementos: dicionario[chave]
    
dicionario = {
    'nome': 'Amanda',
    'idade': 36,
    'cidade': 'Lugar Nenhum'
}

print(dicionario) # Exibe todo o conteúdo do dicionário

print(dicionario['nome']) # Exibe apenas o elemento entre colchetes do dicionário

dicionario['profissao'] = 'programadora' # Adiciona mais um par chave/valor a estrutura do dicionário
print(dicionario)

# Funções de Verificação

chaves = dicionario.keys() # Exibe as chaves do meu dicionário
print(chaves)
valores = dicionario.values() # Exibe os valores contidos no meu dicionário
print(valores)
pares = dicionario.items() # Exibe os valores do par chave/valor do meu dicionário
print(pares)

dicionario_2 = {
    'usuario_1':{
        'nome': 'Ana',
        'idade': 36,
        'cidade': 'Lugar Nenhum',
        'profissao': 'programadora'
    },
    'usuario_2':{
        'nome': 'Mauro',
        'idade': 54,
        'cidade': 'Lugar Algum',
        'profissao': 'escritor'
    }
}

print(dicionario_2)