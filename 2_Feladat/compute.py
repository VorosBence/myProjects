class Compute:
    def __init__(self,database):
        self.database = database
        self.value = 0
        self.index = 0
        self.usedIndex = []
    def searchLoop(self):
        sign = self.database[0][1][:1] == '+'
        number = int(self.database[0][1][1:])
        if self.database[0][0]=='acc':
            self.index += 1
            if sign:
                self.value += number
            else:
                self.value -= number
        elif self.database[0][0]=='jmp':
            if sign:
                self.index += number
            else:
                self.index -= number
        elif self.database[0][0] == 'nop':
            self.index += 1
        self.usedIndex.append(0)


        while True:
            sign = self.database[self.index][1][:1] == '+'
            number = int(self.database[self.index][1][1:])

            if self.database[self.index][0] == 'acc':
                self.index += 1
                if sign:
                    self.value += number
                else:
                    self.value -= number
                    #2. része a Feladatnak ha nop ot talál akk a jmp funkcióját hajtja végre
            elif self.database[self.index][0] == 'jmp' or self.database[self.index][0] == 'nop':
                if sign:
                    self.index += number
                else:
                    self.index -= number
            '''
            1.részben használt kód
            elif self.database[self.index][0] == 'nop':
                self.index += 1
                '''
            if self.index not in self.usedIndex:
                self.usedIndex.append(self.index)
            else:
                break


