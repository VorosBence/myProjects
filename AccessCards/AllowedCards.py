class AllowedCardsCheck():
    def __init__(self,db,allowed):
        self.db = db
        self.allowed = allowed
        self.SuccesLoginCards = []

    def CardsOutPut(self):
        for index,value in enumerate(self.db):
            succesCard = {}
            if index in self.allowed:
                succesCard['id'] = index
                for i in value:
                    if i == 'pid':
                        try:
                            int(value[i])
                            if len(value[i]) == 9:
                                succesCard[i] = 'accepted'
                            else:
                                succesCard[i] = 'denied'
                        except:
                            succesCard[i] = 'denied'

                    if i == 'byr':
                        if len(str(value[i])) == 4 and 1920 < int(value[i]) < 2002:
                            succesCard[i] = 'accepted'
                        else:
                            succesCard[i] = 'denied'
                    if i == 'iyr':
                        if len(str(value[i])) == 4 and 2010 < int(value[i]) < 2021:
                            succesCard[i] = 'accepted'
                        else:
                            succesCard[i] = 'denied'
                    if i == 'eyr':
                        if len(str(value[i])) == 4 and 2021 < int(value[i]) < 2031:
                            succesCard[i] = 'accepted'
                        else:
                            succesCard[i] = 'denied'
                    if i == 'hgt':
                        if value[i][-2:] == 'cm' and 50 < int(value[i][:-2]) < 220:
                            succesCard[i] = 'accepted'
                        elif value[i][-2:] == 'in' and 20 < int(value[i][:-2]) < 90:
                            succesCard[i] = 'accepted'
                        else:
                            succesCard[i] = 'denied'
                    if i == 'hcl':
                        color = value[i][:1]
                        if color == '#':
                            print(value[i])




            if len(succesCard) > 0:
                self.SuccesLoginCards.append(succesCard)





