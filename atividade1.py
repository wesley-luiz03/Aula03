while True:
    nome = input("Digite seu nome: ")
    idade = int(input("Digite sua idade: "))
    salario = float(input("Digite seu salário: "))
    reajuste = int(input("Digite o percentual de reajuste: "))

    novo_salario = ((reajuste * salario / 100) + salario)

    if idade >= 18:
        print(f"Olá! {nome}, você tem {idade} anos e seu novo salário é {novo_salario:.2f}!")
    else:
        print("Sinto muito! Você não pode responder por ser menor de idade!")
        continue