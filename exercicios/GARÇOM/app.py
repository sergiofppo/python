bandejas = int(input("Digite o número de bandejas: "))

copos_quebrados = 0

for i in range(bandejas):
    latas = int(input(f"Digite o número de latas na bandeja {i + 1}: "))
    copos = int(input(f"Digite o número de copos na bandeja {i + 1}: "))

    if latas > copos:
        copos_quebrados += copos
        print(f"O número de copos quebrados foi de: {copos_quebrados}!")
    else:
        print("Nenhum copo foi quebrado!")
    