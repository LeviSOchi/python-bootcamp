import json

produto_01: dict = {
    "nome":"sapato",
    "quantidade":39,
    "preco":10.38,
    "disponibilidade": True
}

produto_02: dict = {
    "nome":"computador",
    "quantidade":12,
    "preco":100.43,
    "disponibilidade": True
}

carrinho:list = []

carrinho.append(produto_01)
carrinho.append(produto_02)

carrinho_json = json.dumps(carrinho)
print(carrinho_json)

