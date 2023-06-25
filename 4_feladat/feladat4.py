numbers = []

with open('lottosz.dat','r') as file:
    for line in file:
        number = line.strip().split()
        number = [int(i) for i in number]
        numbers.append(number)

#feladat1

#het_52 = input('Irja be az 52. het nyerőszámait: ')
het_52 = '89 24 34 11 64'
het52szamok = [int(x) for x in het_52.strip().split()]
#feladat2
het52szamok.sort()
print(f'{het52szamok} rendezett számok')


#feladat3
#szam = int(input('Irj be egy egész számot 1 -51 között: '))
szam = 2
print(f'{numbers[szam-1]} {szam} hét')

#5 feladat
kihuzottszamok = []
for i in numbers:
    for x in i:
        if x not in kihuzottszamok:
            kihuzottszamok.append(x)

nemkihuzottszamok = [x for x in range(1,91) if x not in kihuzottszamok]
'''for x in range(1,91):
    if x not in kihuzottszamok:
        nemkihuzottszamok.append(x)'''
print(f'{nemkihuzottszamok} ezeket a számokat nem húzták ki')

#6 feladat
paratlan = 0
paros = 0
for x in kihuzottszamok:
    if x %2== 1:
        paratlan+=1
    else:
        paratlan+=1






#feladat 7
numbers.append(het52szamok)
with open('lotto52.ki',"w") as file:
    for x in numbers:
        print(*x, sep=' ', file=file)

#feladat8
sum_numbers = []

for x in range(1,91):
    count = 0
    for num in numbers:
        for n in num:
            if n == x:
                count +=1
    sum_numbers.append(count)

count = 0
for x in sum_numbers:
    count+=1
    print(x,end=' ')
    if count == 15:
        print(end='\n')
        count = 0



def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

prime_numbers = [n for n in range(1, 91) if is_prime(n)]

for x in nemkihuzottszamok:
    if x in prime_numbers:
        print(f'Ezt a számot nem húzták ki a prímszáok közül {x}')
