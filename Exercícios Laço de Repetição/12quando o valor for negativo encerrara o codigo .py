import os
os.system("cls||clear")
soma:int=0
contador:int=0

while True:
    numero=int(input("Digite um Número: "))
    
    if numero>=0:
        soma+=numero
        contador+=1
    else:
        break    

    media=numero/contador    
    print("Média: ",media)