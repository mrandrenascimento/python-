import os
os.system("cls")


soma=0
notas=[]


for i in range(3):
    nota=float(input("Digite uma nota: "))
    notas.append(nota)
    soma+=notas[i]
media=soma/3    


for i in range(3):
    print(f"Nota: {notas[i]}")    

print(f"Média: {media}")