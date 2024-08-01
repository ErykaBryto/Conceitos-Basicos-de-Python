'''Crie um dicionário representando um carrinho de compras.
Adicione produtos (chaves) e quantidades (valores) ao carrinho.
Calcule o total do carrinho de compra.'''

# Cria um dicionário para o carrinho de compras
carrinho_de_compras = {
    "maçã": 2.50,  # Preço por unidade
    "banana": 1.20,
    "laranja": 3.00,
    "pão": 0.80
}

# Cria um dicionário para armazenar os produtos e quantidades
quantidades = {
    "maçã": 4,
    "banana": 6,
    "laranja": 3,
    "pão": 10
}

# Calcula o total do carrinho de compras
total = sum(carrinho_de_compras[produto] * quantidades[produto] for produto in carrinho_de_compras)

# Exibe o total
print(f"O total do carrinho de compras é: R$ {total:.2f}")
