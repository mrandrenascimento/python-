import os

#função sem retorno
def logoSenai():
    os.system("cls||clear")
    print("=== ===== ===")
    print("=== SENAI ===")
    print("=== ===== ===")

#função com retorno
def somar(n1,n2):
    resultado = n1 + n2
    return resultado

def sub(n1,n2):
    resultado=n1-n2
    return resultado

def mult(n1,n2):
    return n1*n2 

def div(n1,n2):
    return n1/n2

#Solicitando dados para o usuario
    
logoSenai()
primeiroNumero=int(input("Digite o Primeiro Número: "))
logoSenai()
segundoNumero=int(input("Digite o Segundo Número: "))

soma=somar(primeiroNumero,segundoNumero)
subtacao=sub(primeiroNumero,segundoNumero)
multiplicacao=mult(primeiroNumero,segundoNumero)
divisao=div(primeiroNumero,segundoNumero)

#Exibindo dados para o usuario

#logoSenai()
print(f"Soma: {soma}")

#logoSenai()
print(f"Subtração: {subtacao}")

#logoSenai()
print(f"Multiplicação: {multiplicacao}")

#logoSenai()
print(f"Divisão: {divisao:.2f}")
