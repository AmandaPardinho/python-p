# Condicionais 2
    # Match/Case
    # Igual Switch/Case do Java/C#

tipo = input("Qual tipo de produto você comprou? ")

match tipo:
    case "Laranja":
        print("Fruta")
    case "Cenoura":
        print("Legumes")
    case "Patinho":
        print("Carnes")
    case "Coca-Cola":
        print("Refrigerantes")
    case "Bud":
        print("Cervejas")
    
match tipo:
    case "Laranja" | "Maçã" | "Banana":
        print("Fruta")
    case "Cenoura" | "Batata" | "Abóbora":
        print("Legumes")
    case "Patinho" | "Alcatra" | "Picanha":
        print("Carnes")
    case "Coca-Cola" | "Guaraná" | "Fanta":
        print("Refrigerantes")
    case "Bud" | "Original" | "Baden Baden":
        print("Cervejas")