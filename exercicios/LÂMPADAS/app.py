cliques = input()
operacoes = input().split()
A = False
B = False
for i in operacoes:
    if i == "1":
        A = not A
    else:
        A = not A
        B = not B
print(int(A))
print(int(B))