palavras_guia, palavras_irregulares = [int(x) for x in input().split()]
guia = {}
saida = []
for x in range(palavras_guia):
    irregular, plural = input().split()
    guia[irregular] = plural
for x in range(0, palavras_irregulares):
    palavra_singular = input()
    ultima_letra = palavra_singular[len(palavra_singular)-1]
    ultima_silaba = palavra_singular[len(palavra_singular)-2 : len(palavra_singular)]
    if palavra_singular in guia.keys():
        saida.append(guia[palavra_singular])
    elif (ultima_letra == 'y') and (palavra_singular[len(palavra_singular)-2] not in 'aeiou' ):
        saida.append(palavra_singular[0:len(palavra_singular)-1]  + 'ies')
    elif ((ultima_letra == 'o') or (ultima_letra == 's') or (ultima_letra == 'x')) or (ultima_silaba == ('ch') or  (ultima_silaba == 'sh')):
        saida.append(palavra_singular+'es')
    else:
        saida.append(palavra_singular+'s')

for x in saida:
    print(x)