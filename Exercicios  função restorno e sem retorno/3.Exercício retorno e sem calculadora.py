import os
def cabecalho():
    os.system("cls||clear")
    print("=== ===== ===")
    print("=== SENAI ===")
    print("=== ===== ===")

def tabuada(numero):
    for i in range (10):
        print(f"{numero} X {i+1} = {numero*(i+1)}")


cabecalho()
numero=int(input("Digite um Número: "))

numero=tabuada(numero)
       
