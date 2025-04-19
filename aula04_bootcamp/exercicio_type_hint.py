# O uso de Type Hint ajuda a tornar o código mais legível e seguro, especificando o tipo de dados esperados por funções e variáveis.

# Exercício será tipar o desafio da aula 03
nome_valido: bool = False
salario_valido: bool = False
bonus_valido: bool = False

# Enquanto a variável nome_valido continuar False o fluxo continua
while nome_valido is not True:
    try:
        # Solicita ao usuário que digite seu nome
        nome: str = input("Digite seu nome: ")
        # Verifica se o nome está vazio
        if len(nome) == 0:
            raise ValueError("O nome não pode estar vazio.")
        # Verifica se só digitou espaço
        elif nome.isspace():
            raise ValueError("Você só digitou espaço")
        # Verifica se há números no nome
        elif any(char.isdigit() for char in nome):
            raise ValueError("O nome não deve conter números.")
        else:
            # Se não houver nenhum erro, variável se torna True e encerra o fluxo
            nome_valido = True
    except ValueError as e:
        print(e)

# Solicita ao usuário que digite o valor do seu salário e converte para float

# Enquanto a variável nome_valido continuar False o fluxo continua
while salario_valido is not True:
    try:
        salario: float = float(input("Digite o valor do seu salário: "))
        # Verifica se o usuário digitou número negativo
        if salario < 0:
            print("Por favor, digite um valor positivo para o salário.")
        else:
            # Se não houver nenhum erro, variável se torna True e encerra o fluxo
            salario_valido = True
    except ValueError:
        print("Entrada inválida para o salário. Por favor, digite um número.")

# Solicita ao usuário que digite o valor do bônus recebido e converte para float
while bonus_valido is not True:
    try:
        bonus: float = float(input("Digite o valor do bônus recebido: "))
        # Verifica se o usuário digitou número negativo
        if bonus < 0:
            print("Por favor, digite um valor positivo para o bônus.")
        else:
            # Se não houver nenhum erro, variável se torna True e encerra o fluxo
            bonus_valido = True
    except ValueError:
        print("Entrada inválida para o bônus. Por favor, digite um número.")

bonus_recebido: float = 1000 + salario * bonus  # Exemplo simples de KPI

# Imprime as informações para o usuário
print(f"{nome}, seu salário é R${salario:.2f} e seu bônus final é R${bonus_recebido:.2f}.")


