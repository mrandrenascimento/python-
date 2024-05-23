import os
os.system("cls||clear")

while True:

    nota=float(input("Digite a Nota (entre 0 e 10): "))

    if nota <0 or nota>10:
        print(f"Nota Invalida {nota}")
    else:
        print(f"Nota Imformada: {nota}")
        break    
    
    

