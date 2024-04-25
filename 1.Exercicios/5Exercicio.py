import os
os.system("cls||clear")
 

descricaoProduto=str(input("Digite o Item Desejado:  "))
quantidadeAdiquirida=float(input("Digite Quantidade:  "))
valorUnitario=float(input("Digite Valor Unitário:  "))

total=quantidadeAdiquirida*valorUnitario

if quantidadeAdiquirida<=5:
        desconto=0.02
elif quantidadeAdiquirida>5 and quantidadeAdiquirida<=10:
        desconto=0.03

else:
    desconto=0.05

totalApagar=total-(total*desconto)

"""
soma=primeiroNumero+segundoNumero
multiplicacao=primeiroNumero*segundoNumero
media=soma/2
"""



print(f"Descrição do Produto: {descricaoProduto}")
print(f"Quantidade Adquirida: {quantidadeAdiquirida}")
print(f"Valor Unitário: {valorUnitario}")
print(f"Total : {total}")
print(f"Total a Pagar: {totalApagar}")

