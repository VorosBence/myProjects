class Compute:
    def __init__(self,database):
        self.database = database
        self.value = 0
        self.index = 0
    def searchLoop(self):
        sign = self.database[0][1][:1] == '+'
        number = int(self.database[0][1][1:])
        if self.database[0][0]=='acc':
            if sign:
                self.index += 1
                self.value += number
            else:
                self.index -= 1
                self.value -= number
        elif self.database[0][0]=='jmp':
            if sign:
                self.index += number
            else:
                self.index -= number
        elif self.database[0][0] == 'nop':
            self.index += 1






