import os
os.system("cls||clear")
 

descricaoProduto=str(input("Digite o Item Desejado:  "))
quntidadeMorango=float(input("Digite Quantidade:  "))
valorMorango=float(input("Digite Valor Unitário:  "))

total=quantidadeAdiquirida*valorUnitario

if quantidadeAdiquirida<=5:
        desconto=2.50
elif quantidadeAdiquirida>5 and quantidadeAdiquirida<=10:
        desconto=2.20

else:
    desconto=0.05

totalApagar=total-(total*desconto)




print(f"Descrição do Produto: {descricaoProduto}")
print(f"Quantidade Adquirida: {quantidadeAdiquirida}")
print(f"Valor Unitário: {valorUnitario}")
print(f"Total : {total}")
print(f"Total a Pagar: {totalApagar}")

