import os
def cabecalho():
    os.system("cls||clear")
    print("=== ===== ===")
    print("=== SENAI ===")
    print("=== ===== ===")

def verificarPares(numeros):
    pares=0
    for numero in numeros:
        if numero %2==0:
            pares+=1
    return pares        

def verificarImpares(numeros):
    impares=0
    for numero in numeros:
        if numero %2!=0:
            impares+=1
    return impares        

QUANTIDADENUMEROS=6

listaNumeros=[]

cabecalho()
for i in range (QUANTIDADENUMEROS):
    numero=int(input("Digite um Número: "))
    listaNumeros.append(numero)

quantidadePares=verificarPares(listaNumeros)
quantidadeImpares=verificarImpares(listaNumeros)

cabecalho()
print(f"Quantidade Pares: {quantidadePares}")
print(f"Quantidade Impares: {quantidadeImpares}")



