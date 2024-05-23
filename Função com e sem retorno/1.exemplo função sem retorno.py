import os
#função sem retorno
def logoSenai():
    os.system("cls||clear")
    print("=== ===== ===")
    print("=== SENAI ===")
    print("=== ===== ===")

    #Solicitando dados para o usuario
logoSenai()
nome=input("Digite seu Nome: ")
    
logoSenai()
idade=int(input("Digite sua Idade: "))
    
logoSenai()
peso=float(input("Digite seu Peso: "))

    #Exibindo dados para o usuario
logoSenai()
print(f"Nome: {nome}")
print(f"Idade: {idade}")
print(f"Peso: {peso:.2f}")