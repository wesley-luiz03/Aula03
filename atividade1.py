nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
salario = float(input("Digite seu salário: "))

if idade >= 18:
    print(f"Olá! {nome}, você tem {idade} (maior de idade) anos e recebe {salario}!")
else:
    print(f"Olá! {nome}, você tem {idade} (menor de idade) anos e recebe {salario}!")
