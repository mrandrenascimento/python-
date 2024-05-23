import os
os.system("cls||clear")
soma=0
valor:int=0
quantidadeInserida:int=0

#while (valor>0):
#valor:int=-1

while (valor>0):
    valor=int(input("Digite a Nota (entre 0 e 10 para dar Seguimento ao laço): "))
    quantidadeInserida+=1
    soma+=valor

media=soma/quantidadeInserida    

print(f"Média Aritmetica: {media}")

