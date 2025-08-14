# Boolean
    # True or False
    # 0 (false) or 1 (true)
    
# def calcular():
#     num_1 = int(input("Digite um número: "))
#     if(num_1 % 2 == 0):
#         print("O número digitado é par.")
#     else:
#         print("O número digitado é ímpar")
        
# calcular()

def calcular():
    num_1 = int(input("Digite um número: "))
    if ehPar(num_1):
        print(f"{num_1} é par.")
    else:
        print(f"{num_1} é ímpar")
        
# def ehPar(x:int):
#     if(x % 2 == 0):
#         return True
#     else:
#         return False
    
def ehPar(y:int):
    return True if y % 2 == 0 else False
    
calcular()
