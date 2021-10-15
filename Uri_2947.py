qtdquestoes = int(input())
burro = list(input())
colegas = int(input())

chance = 0
gabaritos = []
respostas = []
respostassub = []

for x in range(colegas):
    gabarito = list(input())
    gabaritos.append(gabarito[:])

for x in range(qtdquestoes):
    for y in range(colegas):
        respostassub.append(gabaritos[y][x]) 
    respostas.append(respostassub[:])
    respostassub.clear()

for x in range(qtdquestoes):
    count = 0
    maior = respostas[x][0]
    for i in respostas[x]:
        if (respostas[x].count(i) > count) and (i != burro[x]):
            count = respostas[x].count(i)
    chance += count        

print(chance)

