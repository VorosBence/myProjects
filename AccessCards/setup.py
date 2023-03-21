from Cards import *
from loginReturn import *

def allowedCards():

    print(f'A rendszerben {l1.allowed} belépő kértya van rendben')
    print(f'{l1.denied} db azoknak a kártyáknak a száma amik nincsenek rendben')

if __name__ == '__main__':
    c1 = cardsData()
    c1.readFile()
    db = c1.database

    l1 = loginReturn(db)
    l1.argsCheck()
    l1.searchError()
    l1.loginCardsOK()

    allowedCards()
