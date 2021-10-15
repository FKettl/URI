real, centavos = [int(x) for x in input().split('.')]
listreais = [100, 50, 20, 10, 5, 2, 1]
listcentavos = ['50', '25', '10', '05', '01']
usoureais = {}
usoucentavos ={}
for x in listreais:
    usoureais[x] = (real // x) 
    real -= (usoureais[x]*x)
for x in listcentavos:
    y = int(x)
    usoucentavos[x] = (centavos//y)
    centavos -= (usoucentavos[x]*y)

print('NOTAS:')
for x in usoureais:
    if x != 1:
        print(f'{usoureais[x]:.0f} nota(s) de R$ {x}.00')
print('MOEDAS:')
print(f'{usoureais[1]} moeda(s) de R$ 1.00')
for x in usoucentavos:
    print(f'{usoucentavos[x]} moeda(s) de R$ 0.{x}')