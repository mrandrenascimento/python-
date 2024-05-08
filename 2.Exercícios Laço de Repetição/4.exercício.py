import os
os.system("cls||clear")

pares=0
impares=0
for i in range(5):
    numeros=int(input(f"Digite o {i+1}º Número: "))
    
    if numeros % 2 == 0:
        pares+=1
    else:
        impares+=1    

    
print(f"Quantidade de Pares: {pares}")
print(f"quantidade de impares: {impares}")