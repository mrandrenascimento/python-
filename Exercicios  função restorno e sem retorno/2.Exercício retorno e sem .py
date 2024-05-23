import os

def cabecalho():
    os.system("cls||clear")
    print("=== ===== ===")
    print("=== SENAI ===")
    print("=== ===== ===")

def med(n1,n2):
    soma=n1+n2
    resultado=soma/2
    return resultado

cabecalho()
primeiroNumero=int(input("Digite o Primeiro Número: ") )

cabecalho()
segundoNumero=int(input("Digite o Segundo Número: ") )

cabecalho()
media=med(primeiroNumero,segundoNumero)
print(f"Média: {media:.2f}")
