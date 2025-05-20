#Pede pro usuario escrever o numero de numeros
n = int(input())

#Pede pro usuario escrever os numeros sorteados e coloca eles em lista
consecutivos = list(map(int, input().split()))

#Inicializa as variaveis e igual a 1
maxseq = seqatual = 1

#FOR i que começa no 1 e acaba no n-1
for i in range(1, n):

    #SE o consectivo atual for igual ao consecutivo anterior:
    if consecutivos [i] == consecutivos [i -1]:

        #Adiciona +1 na sequencia atual
        seqatual += 1

        #SE NÃO atualiza a sequencia maxima para o mesmo numero da sequencia atual
    else:
        maxseq = max(maxseq, seqatual)
        seqatual = 1

#Iguala a variavel maximasequencia ao numero da sequencia atual e printa
maxseq = max(maxseq, seqatual)
print(maxseq)