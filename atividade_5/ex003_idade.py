def idade_de_uma_pessoa(nascimento):
    ano_atual = 2025
    idade = ano_atual - nascimento
    return idade * 365

print(idade_de_uma_pessoa(1969))