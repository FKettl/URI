n, k = [int(x) for x in input().split()]
torres = [int(x) for x in input().split()]
bonito = True
picvales = []
for count in range(1, len(torres)-1):
    if (torres[count-1] < torres[count]) and (torres[count+1] < torres[count]):
        picvales.append('P')
    if (torres[count-1] > torres[count]) and (torres[count+1] > torres[count]):
        picvales.append('V')
 
if picvales.count('P') != k:
    bonito = False
if picvales.count('V') != k-1:
    bonito = False 
for x in range(len(picvales)-1):
    if picvales[x] == picvales[x+1]:
        bonito = False 

if bonito == True:
    print('beautiful')
else:
    print('ugly')
