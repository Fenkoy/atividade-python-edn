peso = float(input("Digite seu peso: "))
alt = float(input("Digite sua altura: "))

imc = round(peso / (alt ** 2), 2)

if imc <= 18.5:
    classificacao = "Peso abaixo do ideal, precisa comer mais arroz e feijão"
elif imc <= 25:
    classificacao = "Peso ideal"
elif imc <=30:
    classificacao = "Acima do ideal, sobrepeso ja seu pelancudo"
else:
    classificacao = "KKK ta imenso filho, que isso"

print(f"O seu imc é {imc} - {classificacao}")