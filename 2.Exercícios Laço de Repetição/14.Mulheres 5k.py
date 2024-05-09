
import os
import sys

os.system("cls || clear")

maiorIdade = 0
menorIdade = sys.maxsize
mulheres5k = 0
somaSalarios = 0
quantidadeSalarios = 0
mediaSalarios = 0

while True:
    print("Código \t Descrição")
    print("1 \t Adicionar pessoa")
    print("2 \t Exibir resultados e sair")
    opcao = int(input("Digite a opção desejada: "))
   
    match(opcao):
        case 1:
            print("=== Solicitando dados ===")
            idade = int(input("Digite a idade: "))
            while (idade <=0):
                if idade<=0:
                    idade = int(input("Digite a idade: "))        
           
            sexo = input("Digite o sexo (M ou F): ")
            while (sexo !="f" and sexo !="M"):
                 if sexo !="f" and sexo !="M":
                    sexo = input("Digite o sexo (M ou F): ")      
           
            salario = float(input("Digite o salário: "))
            while(salario<0):
                if salario<0:
                    salario = float(input("Digite o salário: "))
            sexo = sexo.upper()
            somaSalarios += salario
            quantidadeSalarios += 1

            maiorIdade = max(idade, maiorIdade)
            menorIdade = min(idade, menorIdade)

            if sexo == "F" and salario >= 5000:
                mulheres5k += 1

            if quantidadeSalarios != 0:
                mediaSalarios = somaSalarios / quantidadeSalarios
       
        case 2:
            print("=== Mostrando resultados ===")
            print(f"Média de salários do grupo: {mediaSalarios}")
            print(f"Maior idade do grupo: {maiorIdade}")
            print(f"Menor idade do grupo: {menorIdade}")
            print(f"Mulheres com salário a partir de 5 mil: {mulheres5k}")
            break
        case _:
            print("Opção inválida. \nTente novamente.")
"""
import os
import sys
somaSalario=0
quantidadSalario=0        
mulheres5k=0
os.system("cls")
while True:
    print("código \t Descrição")
    print("1 \t Adicionar Pessoa")
    print("2 \t Exibir o resultado e Sair")
    opcao=int(input("Digite a Opção Desejada: "))

    match(opcao):
        case 1:
            
            idade=int(input("Digite sua Idade: "))
            if idade<0:
                idade=int(input("Digite sua Idade: "))
            
            sexo=str(input("Digite F os M para o Sexo: "))
            if sexo !="f" and sexo !="m":
                sexo=str(input("Digite F os M para o Sexo: "))

            salario=float(input("Digite o Seu Salario: "))
            if salario<0:
                salario=float(input("Digite o Seu Salario: "))
            sexo=sexo.upper()
            somaSalario+=salario
            quantidadSalario+=1        

            maiorIdade=max(idade,maiorIdade)
            menorIdade=min(idade,menorIdade)
            
            if sexo=="f" and salario>=5000:
                mulheres5k+=1

            if quantidadSalario!=0:
                mediaSalario=somaSalario/quantidadSalario

        case 2:

            print("Média de Salário Grupo: ",mediaSalario)            
            print("Média de Salário Grupo: ",mediaSalario)            
"""