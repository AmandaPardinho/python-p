# Teste Unitários
    # Verificação de funcionalidades
    # Garantia de qualidade
    # Detecção de falhas
import math

def main():
    x = int(input("Informe o valor de x: "))
    print(f"{x} ao quadrado é igual a %.0f" % quadrado(x))
    
def quadrado(y):
   return math.pow(y, 2) 
   #return y + y # estrutura propositalmente errada

if __name__ == '__main__':
    main()