import os
os.system("cls||clear")
QUANTIDADE_NOTAS =3
soma=0

for i in range(QUANTIDADE_NOTAS):
    
    while True:

        nota=float(input(f"Digite a {i+1}ª Nota (entre 0 e 10): "))


        if nota <0 or nota>10:
            print("Favor Digitar as Notas entre 0 e 10")
        else:
            soma+=nota
            break    

media=soma/QUANTIDADE_NOTAS 
if media >=7:
    resultado="Aprocvado!"

elif media >=5:
    resultado="Recuperação!"
    
else:
    resultado="Reprovado!"
             

print("Média Aritmética",media)
print(f"O Aluno Está:{resultado}")    
    

