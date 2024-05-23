import os
os.system("cls||clear")
soma=0
contador=0
pares=0
impares=0
somaImpares=0
somaPares=0
somaGeral=0
quantidadeGeral=0
while True:
    numero=int(input("Digite um Número: "))
    
    if numero>0:
        
        somaGeral+=numero
        quantidadeGeral+=1
        if numero %2==0:
            somaPares+=numero
            pares+=1
            #resultado=pares
        else:
            impares+=1
            #resultado=impares    
            #somaImpares+=impares
    if numero==0:
       break 
mediaPares=pares/quantidadeGeral
mediaGeral=somaGeral/quantidadeGeral   

print(f"Quantidade Pares: {somaPares}")
print(f"Qauntidade Impares: {somaImpares} ")
print(f"Média Geral: {mediaGeral}")