produto = "camiseta"
preco = 50.00
desconto = round(preco * 0.20 , 2)
preco_final = round(preco - desconto, 2)
print(f"Produto: {produto}")
print(f"Desconto: R${desconto}")
print(f"Preço final com desconto R${preco_final}")