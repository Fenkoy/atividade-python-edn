import requests

def consulta_cep(cep):
    url = f"https://viacep.com.br/ws/{cep}/json/"
    resposta = requests.get(url)

    if resposta.status_code == 200:
        dados = resposta.json()
        if "erro" in dados:
            print("Cep nao encontrado")
        else:
            print(f"O logradouro: {dados['logradouro']}")
            print(f"O bairro: {dados['bairro']}")
            print(f"A cidade: {dados['localidade']}")
            print(f"Estado: {dados['uf']}")
    else:
        print("Erro ao acessar a API.")

cep = input("Digite o CEP: ")
consulta_cep(cep)