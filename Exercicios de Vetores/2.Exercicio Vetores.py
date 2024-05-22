"""
    maiorNumero = max(numero, maiorNumero)
    menorNumero = min(numero, menorNumero)
#media=sum(numeros)/QUANTIDADE_NUMEROS    
"""
import os
import sys
os.system("cls")
#crinado uma constante 
QUANTIDADE_NUMEROS=5

maiorNumero=0
menorNumero=9999
numeros=[]


for i in range(QUANTIDADE_NUMEROS):
    numero=float(input("Digite um Número: "))
    numeros.append(numero)

    if numero>maiorNumero:
        maiorNumero=numero
    else:
        menorNumero=numero    


for numero in numeros:
    print(f"Numero: {numero}")    

print(f"Maior Número: {maiorNumero}")
print(f"Menor Número: {menorNumero}")