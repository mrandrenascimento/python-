import os
os.system("cls||clear")

contadorNotas=0
soma=0
nota=0


while True:
    nota=float(input(f"Digite Sua Nota: "))
    resposta=input(f"Deseja Inserir Mais uma Nota? ")
    #converte o texto digitado em maiusculo
    resposta=resposta.upper()

    soma+=nota
    contadorNotas+=1
    
    if resposta=='n':
        break


media=soma/contadorNotas

print(f"Qauntidade de Notas Inseridas: {contadorNotas}")        
print(f"Média: {media}")        