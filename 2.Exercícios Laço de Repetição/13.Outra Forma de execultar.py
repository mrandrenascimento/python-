import os
os.system("cls||clear")
soma=0
contador=0
pares=0
impares=0
somaImpares=0
somaPares=0

while True:
    numero=int(input("Digite um Número: "))
    
    if numero!=0:
        soma+=numero
        contador+=1
        if numero %2==0:
            pares+=1
            #resultado=pares
            somaPares+=pares
        else:
            impares+=1
            #resultado=impares    
            somaImpares+=impares
    else:
        break    
mediaPares=pares/contador
mediaImpares=impares/contador    
mediaGeral=(somaPares+somaImpares)/contador   
print("Qauntidade Pares: ",somaPares)
print("Qauntidade Impares: ",somaImpares)
print("Média Geral: ",mediaGeral)