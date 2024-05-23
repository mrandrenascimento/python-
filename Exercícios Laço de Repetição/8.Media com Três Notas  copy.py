import os
os.system("cls||clear")
contador=0
soma=0


    
while True:

        numero=int(input(f"Digite um  Número Positivo: "))


        if numero >0 :
           
            contador+=1
        else:
            soma+=numero
            break    

media=soma/contador 

print("Média Aritmética",media)

    

