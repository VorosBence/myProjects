from Cards import *
from loginReturn import *

c1 = cardsData()
c1.readFile()
db = c1.database

l1 = loginReturn(db)
l1.argsCheck()

print(l1.log)
