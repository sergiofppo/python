turma = ('André', 'Fernanda', 'Luiz')
aluno = input("Digite o nome de um aluno: ")
if aluno in turma:
    print(f"O aluno {aluno} está na turma.")
else:
    print(f"O aluno {aluno} não está na turma.")