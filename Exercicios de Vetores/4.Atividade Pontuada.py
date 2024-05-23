import os
import sys
QUANTIDADE_NUMEROS=5
os.system("clear")
quantidadeNumero=0
somaNumero=0
somaPares=0
somaImpares=0
pares=0
impares=0
maioNumero=0
menorNumero=sys.maxsize
numeros=[]

for i in range(QUANTIDADE_NUMEROS):
    numero=int(input(f"Digite o {i+1}º Número: "))
    quantidadeNumero+=1
    somaNumero+=numero
    if numero %2==0:
        pares+=1
        somaPares+=numero
    else:
        impares+=1
        somaImpares+=numero   
    numeros.append(numero)
maioNumero=max(numeros)
menorNumero=min(numeros)
print(f"Quantidade Pares: {quantidadeNumero}")
print(f"Quantidade Impares: {somaNumero}")