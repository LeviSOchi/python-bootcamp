import csv

path_arquivo = "vendas.csv"

# Primeira função que lê o arquivo csv
def ler_csv(nome_do_arquivo_csv: str) -> list[dict]:
    """
    Função que le um arquivo csv 
    e retorna uma lista de dicionario
    """
    lista = []
    
    with open(nome_do_arquivo_csv, mode= 'r', encoding= "utf-8") as arquivo:
        leitor = csv.DictReader(arquivo)
        for linha in leitor:
            lista.append(linha)
    return lista

# Função que filtra os produtos entregues
def processar_dados(lista: list[dict]) -> list[dict]:
    """
    Função que filtra produtos entregues = True
    """
    lista_de_produtos_entregues = []
    for produto in lista:
        if produto.get("entregue") == "True":
            lista_de_produtos_entregues.append(produto)
    return lista_de_produtos_entregues

# Função que soma os valores do produtos
def soma_valor_dos_produtos_entregues(lista_de_produtos_entregues: list[dict]) -> int:



    """
    Uma soma do valor de todos os os produtos entregues
    """
    valor_total = 0
    for produto in lista_de_produtos_entregues:
        valor_total += int(produto.get("preco"))
    return valor_total
