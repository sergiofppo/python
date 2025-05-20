raizes = int(input("Digite o número de raízes:  "))

for _ in range(raizes):
    numero = float(input("Digite um número: "))
    resultado = numero * numero
    print(f"A raiz quadrada de {numero} é: {resultado}!")
