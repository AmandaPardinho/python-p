# Loops
    # While: não sabemos o número exato de repetições
    # For: sabemos o número exato de repetições
    
x = 5

while x != 15:
    print(f"{x} é diferente de 15")
    x += 1

for x in [1, 2, 3, 4, 5]:
    print("Oi")
    
for x in range(3):
    print("Não")
    
while True:
   idade = int(input("Informe a sua idade: ")) 
   if(idade < 18):
       print("Menor de idade")
   else:
       break

