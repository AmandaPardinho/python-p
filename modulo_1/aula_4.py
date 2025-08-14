# Funções

animais = []

def cadastrar_animal(nome, especie, idade):
    animal = {
        'nome': nome,
        'espécie': especie,
        'idade': idade
    }
    animais.append(animal)
    print(f'Animal {nome} cadastrado com sucesso!')
    
cadastrar_animal('Rex', 'cachorro', 12)
cadastrar_animal('Mimi', 'gato', 5)
cadastrar_animal('Loro', 'ave', 30)