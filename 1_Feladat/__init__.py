from readFile import *
from checkFile import *
if __name__ == '__main__':
    db = read_file('feladat1.txt')
    accept,denied,len_accept,len_denied = checkFiles(db)
    allowed,rejected,len_allowed,len_rejected = checkId(db,accept)
    print(f'A rendszerben {len_accept} belépő kértya van rendben')
    print(f'{len_denied} db azoknak a kártyáknak a száma amik nincsenek rendben \n')
    print(f'{len_allowed} belépőkártya van rendben')
    print(f'{len_rejected} belépőkártya nincs rendben')
