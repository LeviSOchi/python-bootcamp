import json

produtos = {
    "livro_01":{"nome":"sapato",
    "preco": 39.99,
    "quantidade":20,
    "disponibilidade": True},

    "livro_02":{"nome":"camiseta",
    "preco": 10.99,
    "quantidade":20,
    "disponibilidade": True}
}

carrinho = []
carrinho.append(produtos["livro_01"])
carrinho.append(produtos["livro_02"])

json_arquivo = json.dumps(carrinho)
print(json_arquivo)