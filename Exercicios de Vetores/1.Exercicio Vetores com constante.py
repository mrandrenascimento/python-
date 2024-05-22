import os
os.system("cls")
#crinado uma constante 
QUANTIDADE_NOTAS=3

soma=0
notas=[]


for i in range(QUANTIDADE_NOTAS):
    nota=float(input("Digite uma nota: "))
    notas.append(nota)
    soma+=notas[i]
media=soma/QUANTIDADE_NOTAS    


for i in range(QUANTIDADE_NOTAS):
    print(f"Nota: {notas[i]}")    

print(f"Média: {media}")