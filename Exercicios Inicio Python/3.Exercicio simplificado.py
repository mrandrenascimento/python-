import os
os.system("cls||clear")
 

primeiroNumero=int(input("Digite a Primeiro Número:  "))
segundoNumero=int(input("Digite a Segundo Número:  "))


soma=primeiroNumero+segundoNumero
multiplicacao=primeiroNumero*segundoNumero
media=soma/2

maiorNumero=max(primeiroNumero,segundoNumero)
menorNumero=min(primeiroNumero,segundoNumero)

"""
if primeiroNumero>segundoNumero:
    maiorNumero=primeiroNumero
else:
    maiorNumero=segundoNumero

if primeiroNumero<segundoNumero:
    menorNumero=primeiroNumero
else:
    menorNumero=segundoNumero   

"""

print(f"Primeiro Número: {primeiroNumero}")
print(f"Sejgundo Número: {segundoNumero}")
print(f"soma: {soma}")
print(f"Multiplicacao: {multiplicacao}")
print(f"Média Aritmetica: {media}")
print(f"Maior Valor: {maiorNumero}")
print(f"Menor Valor: {menorNumero}")

