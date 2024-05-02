import os
os.system("cls||clear")
pesoMorangos=float(input("digite o Peso do Morango: "))
pesoMacas=float(input("digite o Peso do Maçãs: "))

if pesoMorangos< 5:
    precoMorangos=2.50
else: 
    precoMorango=2.2

if pesoMacas< 5:
    precoMacas=1.80
else: 
    precoMacas=1.50

pesoTotal=pesoMorangos+pesoMacas
totalMorango=precoMorango*pesoMorangos
totalMacas=pesoMacas*precoMacas
subtotal=totalMorango+totalMacas

if pesoTotal>8 or subtotal>25:
    desconto=subtotal*0.10

totalPagar=subtotal-desconto

print(f"Peso Morango:{pesoMorangos}")
print(f"Peso Maçãs:{pesoMacas}")
print(f"Peso Total:{pesoTotal}")
print(f"SubTotal:{subtotal:.2f}")
print(f"Desconto:{desconto:.2f}")
print(f"Total a Pagar:{totalPagar:.2f}")