import os
os.system("cls")

#criando uma lista/ vetor

notas=[]

#solicitando 3 notas para o usuario
for i in range(3):
    nota=float(input("Digite uma nota: "))
    notas.append(nota)
  
#exibindo as notas para o usuario.
for i in range(3):
    print(f"Nota: {notas[i]}")    

