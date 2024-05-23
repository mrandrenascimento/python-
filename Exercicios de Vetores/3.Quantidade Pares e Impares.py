
import os

os.system("clear")

#crinado uma constante 
QUANTIDADE_NUMEROS=6
pares=0
impares=0
contador=0
numeros=[]


for i in range(QUANTIDADE_NUMEROS):
   
    numero=float(input("Digite um Número: "))
    if numero %2==0 :
        pares+=1
        
    else:
        impares+=1
        
    numeros.append(numero)

maiorNumero = max(numeros)
menorNumero = min(numeros)


for i, numero in enumerate(numeros):
    print(f"{i+1}º Número: {numero}")    


print(f"Quantidade Pares: {pares}")
print(f"Quantidade Impares: {impares}")
print(f"Maior Número:{maiorNumero}")