while True:
    try:
        n1 = float(input("Digite um numero: "))
        n2 = float(input("Digite outro numero: "))
        operacao = input("Digite a operação desejada ( + | - | * e /): ")

        resultado = None

        if operacao == '+':
            resultado = n1 + n2
        elif operacao == '-':
            resultado = n1 - n2
        elif operacao == '*':
            resultado = n1 * n2
        elif operacao == '/':
            resultado = n1 / n2
        else:
            print("Operação inválida, tente novamente por favor !")
            continue

        print(f"Resultado: {n1} {operacao} {n2} = {resultado}")
        break

    except ValueError:
        print("Erro: entrada inválida")
        continue

    except ZeroDivisionError:
        print("Erro: divisão por  zero não é permitido, tente novamente")
        continue

    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}. Tente novamente")
        continue