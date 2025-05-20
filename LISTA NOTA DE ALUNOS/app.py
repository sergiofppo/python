notas = [6.3, 7.5, 9.2, 5.1, 6.8]
lista = []
media = sum(notas)/len(notas)
print(f"A média do aluno é de: {media:.2f}")
for nota in notas:
    if nota > 6:
        lista.append(nota)
print(f"O número de notas acima de '6' é: {len(lista)}")