constante_bonus = 1000

nome = input("Digite o seu nome: ")

salario = float(input("Digite o seu salário: "))
bonus = float(input("Qual a porcentagem do seu bonus? "))

calculo = constante_bonus + salario * bonus

print(f"Olá {nome}, o seu bônus foi de {calculo}")
