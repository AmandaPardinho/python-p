# Condicionais
    # Controle de fluxo
    # if, elif, else

idade = int(input("Qual a sua idade? "))

if idade > 0 and idade <= 10:
    print('Criança')
elif (idade > 10 and idade <= 13):
    print("Pré-adolescente")
elif (idade > 13 and idade <= 17):
    print("Adolescente")
else:
    print("Adulto")    
