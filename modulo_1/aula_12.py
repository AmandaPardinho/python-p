# Criação manual de um teste unitário

from aula_11 import quadrado

def main():
    teste_quadrado()

"""  
Exemplo de uma função que não usa o assert, mas é equivalente à que usa
 
def teste_quadrado():
    if quadrado(2) != 4:
        print("Bug")
    if quadrado(3) != 9:
        print("Bug")
    if quadrado(5) != 25:
        print("Bug")
    if quadrado(10) != 100:
        print("Bug") 
""" 

def teste_quadrado():
    try:
        assert quadrado(2) == 4
        assert quadrado(3) == 9
        assert quadrado(5) == 25
        assert quadrado(10) == 100
    except AssertionError:
        print("Confira a estrutura da função quadrado()")
    
if __name__ == '__main__':
    main()