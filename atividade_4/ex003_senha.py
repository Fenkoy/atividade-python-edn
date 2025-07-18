

print("Digite uma senha númerica válida de até 8 dígitos")

while True:
    senha = input("Digite uma senha forte ( ou 'sair', para encerrar): ")

    if senha.lower() == "sair":
        break

    if len(senha) < 8:
        print("Senha inválida, tente novamente !")
        continue

    tem_numero = any(char.isdigit() for char in senha)

    if not tem_numero:
        print("Senha Fraca: precisa conter pelo menos um número.")
        continue

    print("Senha forte !")
    break

