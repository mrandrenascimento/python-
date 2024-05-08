import os
os.system("cls||clear")
soma:int=0

for i in range (1,6):
    numero=int(input(f"Digite o {i}º Número "))

    soma=soma+numero
 
print(f"Soma: {soma}")