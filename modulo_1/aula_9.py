# Try Except
    # Tratamento de exceções
    # Captura de erros
    # Garante que o programa não pare abruptamente

while True:
    try:
        x = int(input("Digite um número: "))
    except ValueError:
        print("O usuário não digitou um número inteiro")
    else:
        break

print(f"{x} é um número inteiro")
