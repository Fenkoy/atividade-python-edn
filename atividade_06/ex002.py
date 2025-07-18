import requests

def gerar_perfil():
    resposta = requests.get("https://randomuser.me/api/")
    if resposta.status_code == 200:
        dados = resposta.json()
        usuario = dados["results"][0]
        nome = f"{usuario["name"]["first"]} {usuario["name"]["last"]}"
        email = usuario['email']
        pais = usuario["location"]["country"]
        print(f"Nome: {nome}\nEmail: {email}\nPaís: {pais}")
    else:
        print("Erro ao acesso a API.")

gerar_perfil()