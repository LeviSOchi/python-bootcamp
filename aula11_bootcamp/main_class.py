import pandas as pd

class CsvProcessador:
    def __init__ (self, path_arquivo):
        self.path_arquivo = path_arquivo
        self.df = None

    def carregar_csv(self):
        self.df = pd.read_csv(self.path_arquivo)

    def filtrar_por(self, coluna, atributo):
       return self.df [self.df[coluna] == atributo]
    
arquivo_csv = "./exemplo.csv"
filtro = "estado"
limite = "SP"

arquivo_CSV = CsvProcessador(arquivo_csv)
arquivo_CSV.carregar_csv()
print(arquivo_CSV.filtrar_por(filtro,limite))

arquivo_CSV2 = "./exemplo.csv"
filtro = "estado"
limite = "PR"

arquivo_CSV2 = CsvProcessador(arquivo_CSV2)
arquivo_CSV2.carregar_csv()
print(arquivo_CSV2.filtrar_por(filtro,limite))