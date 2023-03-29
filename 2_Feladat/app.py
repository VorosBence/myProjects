from readFile import *
from compute import *

def value():
    print(f'A belső változó értéke : {App.value} \nÖsszes index száma {len(App.usedIndex)}')

if __name__ == '__main__':
    db = readFile()
    App = Compute(db)
    App.searchLoop()
    value()

