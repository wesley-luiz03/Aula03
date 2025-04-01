time1 = input("Digite o nome do 1º time: ")
time2 = input("Digite o nome do 2º time: ")

qntgols1 = int(input("Digite o número de gols do 1º time: "))
qntgols2 = int(input("Digite o número de gols do 2º time: "))

if qntgols1 > qntgols2:
    print(f"O {time1} venceu!")
else:
    if qntgols1 == qntgols2:
        print("Empate!")
    else:
        print(f"O {time2} venceu!")