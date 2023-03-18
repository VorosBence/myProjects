__pid__ = 'kártya azonosító'
__byr__ = 'születési év'
__cid__ = 'születési ország'
__iyr__ = 'kártya kiállításának éve'
__eyr__ = 'lejárati dátum'
__hgt__ = 'magasság'
__hcl__ = 'hajszín'
__ecl__ = 'szemszín'

__arg__ = ['pid','byr','cid','iyr','eyr','hgt','hcl','ecl']


test = {'ecl': 'amb', 'pid': '690616023', 'byr': '1994', 'iyr': '2014', 'hgt': '172cm', 'hcl': '#c0946f', 'eyr': '2022'}
count = 0
for i in test:

    if i in __arg__:
        print(True)
        count += 1
    elif i not in __arg__:
        print(False)

print(count)