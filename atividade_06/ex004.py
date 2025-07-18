import requests

def consultar_cotacao(moeda):
    url = f"https://economia.awesomeapi.com.br/json/last/{moeda}-BRL"
    resposta = requests.get(url)

    if resposta.status_code == 200:
        dados = resposta.json()
        chave = moeda + "BRL"
        if chave in dados:
            info = dados[chave]
            print(f"Moeda: {info['name']}")
            print(f"Valor atual: R${info['bid']}")
            print(f"Valor Máximo: R${info['high']}")
            print(f"Valor mínimo: R${info['low']}")
            print(f"Data: {info['create_date']}")
        else:
            print("Moeda não encontrada !")
    else:
        print("Erro ao acessar a API !")

moeda = input("Digite o código da moeda ( USD / EUR/ GBP / BRL ): ").upper()
consultar_cotacao(moeda)