from etl import pipeline_de_vendas_consolidado


pasta_argumento = "data"
formato_de_saida: list = ["csv","parquet"]

pipeline_de_vendas_consolidado(pasta_argumento, formato_de_saida)
