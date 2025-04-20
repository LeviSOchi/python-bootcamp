## Exercícios de Listas e Dicionários

#1 Crie uma lista com os números de 1 a 10 e use um loop para imprimir cada número elevado ao quadrado.
numeros: list = list(range(1, 11))
for numero in numeros:
    print(numero**2)

#2 Dada a lista ["Python", "Java", "C++", "JavaScript"], remova o item "C++" e adicione "Ruby".
linguagens = ["Python", "Java", "C++", "JavaScript"]
linguagens.remove("C++")
linguagens.append("Ruby")

print(linguagens)

#3 Crie um dicionário para armazenar informações de um livro, incluindo título, autor e ano de publicação. Imprima cada informação.
livro = {
    "Título":"Harry Potter",
    "Autor":"J. K. Rowling",
    "ano": 2000
}

for chave,valor in livro.items():
    print(f"{chave}:{valor}")

#4 Escreva um programa que conta o número de ocorrências de cada caractere em uma string usando um dicionário.
def contar_caracteres(s):
    contagem = {}
    for caractere in s:
        contagem[caractere] = contagem.get(caractere, 0) + 1
    return contagem

print(contar_caracteres("engenharia de dados"))

#5 Dada a lista ["maçã", "banana", "cereja"] e o dicionário {"maçã": 0.45, "banana": 0.30, "cereja": 0.65}, calcule o preço total da lista de compras.
lista_compras = ["maçã", "banana", "cereja"]
precos = {"maçã": 0.45, "banana": 0.30, "cereja": 0.65}
total = sum(precos[item] for item in lista_compras)
print(f"Preço total: {total}")

## Exercícios intermediários à avançado

#6 Objetivo: Dada uma lista de emails, remover todos os duplicados.
emails = ["user@example.com", "admin@example.com", "user@example.com", "manager@example.com"]
emails_unicos = list(set(emails))

print(emails_unicos)

#7 Objetivo: Dada uma lista de idades, filtrar apenas aquelas que são maiores ou iguais a 18.
idades = [12,14,23,45,23,57,12,23,12,11,69,24]

idades_validas = [idade for idade in idades if idade >= 18]
print("Idades válidas ")

#8 Objetivo: Dada uma lista de dicionários representando pessoas, ordená-las pelo nome.


#9 Objetivo: Dado um conjunto de números, calcular a média.


#10 Objetivo: Dada uma lista de valores, dividir em duas listas: uma para valores pares e outra para ímpares.


#11 Objetivo: Dada uma lista de dicionários representando produtos, atualizar o preço de um produto específico.


#12 Objetivo: Dados dois dicionários, fundi-los em um único dicionário.


#13 Objetivo: Dado um dicionário de estoque de produtos, filtrar aqueles com quantidade maior que 0.


#14 Objetivo: Dado um dicionário, criar listas separadas para suas chaves e valores.


#15 Objetivo: Dada uma string, contar a frequência de cada caractere usando um dicionário.