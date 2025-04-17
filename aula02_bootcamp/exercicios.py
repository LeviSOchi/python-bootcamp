import math

# #### Inteiros (`int`)

# 1. Escreva um programa que soma dois números inteiros inseridos pelo usuário.
print("Vamos somar dois números que você digitar")
soma1 = int(input("Digite um número: "))
soma2 = int(input("Digite outro número: "))
soma = soma1+soma2
print(soma)

# 2. Crie um programa que receba um número do usuário e calcule o resto da divisão desse número por 5.
print("Vamos calcular o resto da divisao do número que você digitar dividido por 5")
resto_divisao1 = int(input("Digite um número: "))
resto_divisao = resto_divisao1%5
print(resto_divisao)

# 3. Desenvolva um programa que multiplique dois números fornecidos pelo usuário e mostre o resultado.
print("Vamos multiplicar dois números que você digitar")
multi1 = int(input("Digite um número: "))
multi2 = int(input("Digite outro número: "))
multiplicacao = multi1*multi2
print(multiplicacao)

# 4. Faça um programa que peça dois números inteiros e imprima a divisão inteira do primeiro pelo segundo.
print("Vamos fazer a divisão inteira do primeiro número pelo segundo número que você digitar")
divisao1 = int(input("Digite um número: "))
divisao2 = int(input("Digite outro número: "))
divisao_inteira = divisao1//divisao2
print(divisao_inteira)

# 5. Escreva um programa que calcule o quadrado de um número fornecido pelo usuário.
print("Vamos fazer a potência do número que você digitar")
potencia1 = int(input("Digite um número: "))
potencia = potencia1**2
print(potencia)

## #### Números de Ponto Flutuante (`float`)

## 6. Escreva um programa que receba dois números flutuantes e realize sua adição.
print("Vamos somar dois números que você digitar")
soma1 = float(input("Digite um número: "))
soma2 = float(input("Digite outro número: "))
soma = soma1+soma2
print(f"{soma:.2f}")

# 7. Crie um programa que calcule a média de dois números flutuantes fornecidos pelo usuário.
n1 = float(input("Digite um número "))
n2 = float(input("Digite outro número "))
media = (n1+n2)/2
print(media)

# 8. Desenvolva um programa que calcule a potência de um número (base e expoente fornecidos pelo usuário).
n1 = float(input("Digite um número "))
n2 = float(input("Digite outro número "))
resultado = n1**n2
print(resultado)

# 9. Faça um programa que converta a temperatura de Celsius para Fahrenheit.
temperatura = float(input("Digite uma temperatura: "))
resultado = temperatura * 1.8 + 32
print(f"Essa temperatura em Fahrenheit seria: {resultado}°F")

# 10. Escreva um programa que calcule a área de um círculo, recebendo o raio como entrada.
print("Vamos calcular a área do raio do círculo que você digitar")
raio_circulo = float(input("Digite o raio do círculo: "))
area_circulo = math.pi  * raio_circulo ** 2
print(f"{area_circulo:.2f}")

# #### Strings (`str`)

# 11. Escreva um programa que receba uma string do usuário e a converta para maiúsculas.
nome = input("Digite seu nome: ")
print(nome.upper())

# 12. Crie um programa que receba o nome completo do usuário e imprima o nome com todas as letras minúsculas.
nome_completo = input("Digite seu nome completo: ")
print(nome_completo.lower())

# 13. Desenvolva um programa que peça ao usuário para inserir uma frase e, em seguida, imprima esta frase sem espaços em branco no início e no final.
frase = input("Digite uma frase: ")
print(frase.strip())

# 14. Faça um programa que peça ao usuário para digitar uma data no formato "dd/mm/aaaa" e, em seguida, imprima o dia, o mês e o ano separadamente.
data = input("Digite uma data no formato dd/mm/aaaa: ")
dia, mes, ano = data.split("/")
print("Dia:", dia)
print("Mês:", mes)
print("Ano:", ano)

# 15. Escreva um programa que concatene duas strings fornecidas pelo usuário.
nome = input("Digite seu primeiro nome: ")
sobrenome = input("Digite seu sobrenome: ")
print("Seja bem-vindo ", nome + sobrenome)

# #### Booleanos (`bool`)

# 16. Escreva um programa que avalie duas expressões booleanas inseridas pelo usuário e retorne o resultado da operação AND entre elas.
valor1 = True
valor2 = False
resultado_and = valor1 and valor2
print("Resultado do AND lógico:", resultado_and)

# 17. Crie um programa que receba dois valores booleanos do usuário e retorne o resultado da operação OR.
valor1 = False
valor2 = True
resultado_or = valor1 or valor2
print("Resultado do OR lógico:", resultado_or)

# 18. Desenvolva um programa que peça ao usuário para inserir um valor booleano e, em seguida, inverta esse valor.
valor1 = False
valor2 = True
resultado_not = not valor1
print("Resultado do NOT lógico:", resultado_not)

# 19. Faça um programa que compare se dois números fornecidos pelo usuário são iguais.
num1 = 5
num2 = 5
resultado_igualdade = (num1 == num2)
print("Resultado da igualdade:", resultado_igualdade)

# 20. Escreva um programa que verifique se dois números fornecidos pelo usuário são diferentes.
num1 = 2
num2 = 5
resultado_diferenca = (num1 != num2)
print("Os números são diferentes?", resultado_diferenca)

# #### try-except e if

# 21: Conversor de Temperatura
# Escreva um programa que converta a temperatura de Celsius para Fahrenheit. O programa deve solicitar ao usuário a temperatura em Celsius e, utilizando try-except, garantir que a entrada seja numérica, tratando qualquer ValueError. Imprima o resultado em Fahrenheit ou uma mensagem de erro se a entrada não for válida.

try:
    temperatura = float(input("Digite uma temperatura: "))
    resultado = temperatura * 1.8 + 32
    print(f"Essa temperatura em Fahrenheit seria: {resultado}°F")
except ValueError:
    print("Por favor, insira um número!")

# 22: Verificador de Palíndromo
# Crie um programa que verifica se uma palavra ou frase é um palíndromo (lê-se igualmente de trás para frente, desconsiderando espaços e pontuações). Utilize try-except para garantir que a entrada seja uma string. Dica: Utilize a função isinstance() para verificar o tipo da entrada.
entrada = input("Digite uma palavra ou frase: ")
if isinstance(entrada, str):
    formatado = entrada.replace(" ", "").lower()
    if formatado == formatado[::-1]:
        print("É um palíndromo.")
    else:
        print("Não é um palíndromo.")
else:
    print("Entrada inválida. Por favor, digite uma palavra ou frase.")

# 23: Calculadora Simples
#Desenvolva uma calculadora simples que aceite duas entradas numéricas e um operador (+, -, *, /) do usuário. Use try-except para lidar com divisões por zero e entradas não numéricas. Utilize if-elif-else para realizar a operação matemática baseada no operador fornecido. Imprima o resultado ou uma mensagem de erro apropriada.
try:
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    operador = input("Digite o operador (+, -, *, /): ")
    if operador == '+':
        resultado = num1 + num2
    elif operador == '-':
        resultado = num1 - num2
    elif operador == '*':
        resultado = num1 * num2
    elif operador == '/' and num2 != 0:
        resultado = num1 / num2
    else:
        print("Operador inválido ou divisão por zero.")
    print("Resultado:", resultado)
except ValueError:
    print("Erro: Entrada inválida. Certifique-se de inserir números.")

# 24: Classificador de Números
try:
    numero = int(input("Digite um número: "))
    if numero > 0:
        print("Positivo")
    elif numero < 0:
        print("Negativo")
    else:
        print("Zero")
    if numero % 2 == 0:
        print("Par")
    else:
        print("Ímpar")
except ValueError:
    print("Por favor, digite um número inteiro válido.")

# 25: Conversão de Tipo com Validação
entrada_lista = input("Digite uma lista de números separados por vírgula: ")
numeros_str = entrada_lista.split(",")
numeros_int = []
try:
    for num in numeros_str:
        numeros_int.append(int(num.strip()))
    print("Lista de inteiros:", numeros_int)
except ValueError:
    print("Erro: certifique-se de que todos os elementos são números inteiros válidos.")

