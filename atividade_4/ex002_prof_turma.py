notas = []

print("Digite as notas da turma (0 a 10). E digite o comando 'Fim' para encerrar.")

while True:
        entrada_nota = input("Digite a nota: ").lower()

        if entrada_nota == "fim":
            break

        try:
            nota = float(entrada_nota)

            if 0 <= nota <= 10:
                notas.append(nota)
            else:
                print("Nota inválida. Digite um valor de 0 a 10.")

        except ValueError:
            print("Entrada Inválida. Digite um número ou 'fim'.")


if len(notas) > 0:
    media = sum(notas) / len(notas)
    print(f"Média da turma é: {media:.2f}")
else:
    print("Nenhuma nota foi registrada:")
