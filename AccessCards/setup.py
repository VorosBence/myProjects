from Cards import *
from loginReturn import *
from AllowedCards import *

def allowedCards():
    print(f'A rendszerben {AppReturn.allowed} belépő kértya van rendben')
    print(f'{AppReturn.denied} db azoknak a kártyáknak a száma amik nincsenek rendben')

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

    for i in AppCheckAll.SuccesLoginCards:
        print(i)