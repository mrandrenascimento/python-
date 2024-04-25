import os
os.system("cls||clear")
 

idade=int(input("Digite a sua Idade:  "))


"""
soma=primeiroNumero+segundoNumero
multiplicacao=primeiroNumero*segundoNumero
media=soma/2

maiorNumero=max(primeiroNumero,segundoNumero)
menorNumero=min(primeiroNumero,segundoNumero)
"""

if idade<18 and idade>65:
    resultado="Não é Obrigado a Votar"
else:
    resultado="Obrigado a Votar"
    



print(f"Idade: {idade}")
print(f"Resultado: {resultado}")

