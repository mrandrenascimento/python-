
import os
import time
import sys
os.system("cls")
#crinado uma constante 
#QUANTIDADE_NUMEROS=5

contador=0
numeros=[]


#for i in range(QUANTIDADE_NUMEROS):

while True:
    
    numero=float(input("Digite um Número: "))
    if numero ==0 :
        break    
        
    numeros.append(numero)

maiorNumero = max(numeros)
menorNumero = min(numeros)


for i, numero in enumerate(numeros):
    print(f"{i+1}º Número: {numero}")    

print(f"Menor Número: {menorNumero}")
print(f"Maior Número: {maiorNumero}")

"""
mudar a estrutura do codigo,nao sabemos a qauntidade de notas que serão inseridas pelo
usuario e para quando o usuario colocar o numero zero
"""