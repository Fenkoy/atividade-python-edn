tempe: float = float(input("Temperatura: "))
origem = input("Unidade de origem (C/F/K): ").upper()
destino = input("Converter para (C/F/K): ").upper()

convertido = None

if origem == "C" and destino == "F":
    convertido = round((tempe * 9/5) + 32, 2)
elif origem == "C" and destino == "K":
    convertido = round(tempe + 273.15, 2)
elif origem == "F" and destino == "C":
    convertido = round((tempe - 32) * 5/9, 2)
elif origem == "F" and destino == "K":
    convertido = round((tempe - 32) * 5/9 + 273.15, 2)
elif origem == "K" and destino == "C":
    convertido = round(tempe - 273.15, 2)
elif origem == "K" and destino == "F":
    convertido = round((tempe - 273.15) * 9/5 + 32, 2)

print(f"A temperatura é {tempe}, a origem é {origem} e então, foi é convertido em: {convertido}")
