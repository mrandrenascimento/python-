import os
os.system("cls||clear")
 
nome=str(input("Digite seu Nome:  "))
idade=int(input("Digite sua Idade:  "))
primeiraNota=int(input("Digite a Primeira Nota:  "))
segundaNota=int(input("Digite a Segunda Nota:  "))

soma=primeiraNota+segundaNota
media=soma/2

print(f"Nome: {nome}")
print(f"idade: {idade}")
print(f"primeira nota: {primeiraNota}")
print(f"segunda nota: {segundaNota}")
print(f"Média Aritmetica: {media}")