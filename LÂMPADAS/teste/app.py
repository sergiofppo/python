cliques = input()
operacoes = input().split()
A = False
B = False
for operacao in operacoes:
    if operacao == "1":
        A = not A
    else:
        A = not A
        B = not B

print("\n")

print(int(A))
print(int(B))