from Cards import *
from loginReturn import *
from AllowedCards import *

def allowedCards():
    print(f'A rendszerben {AppReturn.allowed} belépő kértya van rendben')
    print(f'{AppReturn.denied} db azoknak a kártyáknak a száma amik nincsenek rendben \n\n')

def AllowedCards():
    print(f'{len(AppCheckAll.AllAcceptCards)} belépőkártya van rendben')
    print(f'Itt van az összes belépőkártya indexe: ')
    count = 0
    for value in AppCheckAll.AllAcceptCards:
        count += 1
        if count == 15:
            print(value, end='\n')
            count = 0
        else:
            print(value, end=' ')
if __name__ == '__main__':
    App = cardsData()
    App.readFile()
    db = App.database

    AppReturn = loginReturn(db)
    AppReturn.argsCheck()
    AppReturn.searchError()
    AppReturn.loginCardsOK()

    allowedDB = AppReturn.Allowed

    allowedCards()

    AppCheckAll = AllowedCardsCheck(db,allowedDB)
    AppCheckAll.CardsOutPut()

    AllowedCards()

