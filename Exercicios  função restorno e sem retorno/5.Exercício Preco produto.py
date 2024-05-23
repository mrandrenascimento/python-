import os
def cabecalho():
    os.system("cls||clear")
    print("=== ===== ===")
    print("=== SENAI ===")
    print("=== ===== ===")

def inflac(preco):
    preco=0
    if preco < 100:
       precoTotal=preco*0.01     
    elif preco>=100:
        precoTotal=preco*0.02
    return precoTotal    


cabecalho()

preco=float(input("Digite um Número: "))
inflacao=inflac(preco)


cabecalho()
print(f"Ajuste Inflação: {inflacao}")



