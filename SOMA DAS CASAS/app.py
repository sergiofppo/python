n = int(input())
casas = list(map(int, input().split()))
casas.sort()
somas = []
for _ in range(n):
    for i in range(0, len(casas)- 1, 2):
        soma = casas [i] + casas [i + 1]
        somas.append(soma)
    print(soma)