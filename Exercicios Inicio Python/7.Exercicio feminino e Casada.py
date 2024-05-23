import os
os.system("cls||clear")
nome=str(input("Digite seu Nome: "))
sexo=str(input("Digite S ou F para o Sexo: "))
estadocivil=str(input("Digite seu Estado Civil: "))

sexo=sexo.lower()
if sexo == "f" and estadocivil =="casada":
    tempoCasada=float(input("Digite o tempo de Casada: "))


print(f"Nome Digitado:{nome}")
print(f"Sexo Digitado:{sexo}")
print(f"Estado Civil:{estadocivil}")
if sexo == "f" and estadocivil =="casada":
    print(f"Tempo de Casada: {tempoCasada} ")
