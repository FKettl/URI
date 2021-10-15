dicio = {} 

qtdlinguas = int(input())
for x in range(qtdlinguas):
    linguas = input()
    tradução = input()
    dicio[linguas] = tradução
    
qtdcrianças = int(input())
for x in range(qtdcrianças):
    criança = input()
    lingua = input()
    print(criança)
    print(dicio[lingua])
    print()