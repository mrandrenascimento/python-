import os
os.system("cls||clear")
QUANTIDADE_NOTAS= 2
soma=0
for i in range(QUANTIDADE_NOTAS):
    nota:float=-1
    while (nota<0 or nota>10):
        nota=float(input(f"Digite a {i+1}ª Nota (entre 0 e 10 para dar Seguimento ao laço): "))
    soma+=nota
media=soma/QUANTIDADE_NOTAS    

print(f"Média Aritmetica: {media}")