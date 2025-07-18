def palavra_palindromo(texto):
    texto_limpo = "".join(char.lower() for char in texto if char.isalnum())
    if texto_limpo == texto_limpo[::-1]:
        return "Sim, é palíndromo "
    else:
        return "Não, não é palíndromo"


print(palavra_palindromo("Iago"))
print(palavra_palindromo("Mirim"))
