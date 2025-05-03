from etl import ler_csv, processar_dados, soma_valor_dos_produtos_entregues

path_arquivo = "vendas.csv"

lista_de_produtos = ler_csv(path_arquivo)
filtrar_produtos_entregues = processar_dados(lista_de_produtos)
somar_valores = soma_valor_dos_produtos_entregues(filtrar_produtos_entregues)

print(somar_valores)