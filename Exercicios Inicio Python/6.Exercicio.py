import os
os.system("cls||clear")
 

pesoMorango=float(input("Digite o Item Desejado:  "))
quantidadeMorango=float(input("Digite Quantidade:  "))
valorMorango=float(input("Digite Valor Unitário:  "))

totalMotrango=quantidadeMorango*valorMorango

if quantidadeMorango<=5 and pesoMorango>10:
        desconto=2.50

elif quantidadeMorango>5 and pesoMorango<=10:
        desconto=2.20

else:
        desconto=0.05

totalApagar=total-(total*desconto)




print(f"Descrição do Produto: {descricaoProduto}")
print(f"Quantidade Adquirida: {quantidadeAdiquirida}")
print(f"Valor Unitário: {valorUnitario}")
print(f"Total : {total}")
print(f"Total a Pagar: {totalApagar}")

