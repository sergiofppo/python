N = int(input())
soma_acessos = 0

for i in range(N):
    soma_acessos += int(input())
    if soma_acessos >= 1000000:
        print(i + 1)
        break