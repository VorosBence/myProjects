class AllowedCardsCheck():
    def __init__(self,db,allowed):
        self.db = db
        self.allowed = allowed
        self.SuccesLoginCards = []
        self.AllAcceptCards = []
    def CardsOutPut(self):
        for index,value in enumerate(self.db):
            succesCard = {}
            if index in self.allowed:
                isAccept = 0
                succesCard['id'] = index
                for i in value:
                    if i == 'pid':
                        try:
                            int(value[i])
                            if len(value[i]) == 9:
                                succesCard[i] = 'accepted'
                                isAccept += 1
                            else:
                                succesCard[i] = 'denied'
                        except:
                            succesCard[i] = 'denied'

                    if i == 'byr':
                        if len(str(value[i])) == 4 and 1920 < int(value[i]) < 2002:
                            succesCard[i] = 'accepted'
                            isAccept += 1
                        else:
                            succesCard[i] = 'denied'
                    if i == 'iyr':
                        if len(str(value[i])) == 4 and 2010 < int(value[i]) < 2021:
                            succesCard[i] = 'accepted'
                            isAccept += 1
                        else:
                            succesCard[i] = 'denied'
                    if i == 'eyr':
                        if len(str(value[i])) == 4 and 2021 < int(value[i]) < 2031:
                            succesCard[i] = 'accepted'
                            isAccept += 1
                        else:
                            succesCard[i] = 'denied'
                    if i == 'hgt':
                        if value[i][-2:] == 'cm' and 50 < int(value[i][:-2]) < 220:
                            succesCard[i] = 'accepted'
                            isAccept += 1
                        elif value[i][-2:] == 'in' and 20 < int(value[i][:-2]) < 90:
                            succesCard[i] = 'accepted'
                            isAccept += 1
                        else:
                            succesCard[i] = 'denied'
                    if i == 'hcl':
                        hashtag = value[i][:1]
                        color = value[i][1:]
                        color_alphabets = ['a','b','c','d','e','f']
                        color_nums = [0,1,2,3,4,5,6,7,8,9]
                        colorCheck = 0
                        if hashtag == '#':
                            for color_index in range(6):
                                if color[color_index] in color_alphabets or int(color[color_index]) in color_nums:
                                    colorCheck += 1

                        if colorCheck == 6:
                            succesCard[i] = 'accepted'
                            isAccept += 1
                        else:
                            succesCard[i] = 'denied'
                    if i == 'ecl':
                        ecl_data = ['grn','blu','brn','hzl','oth','amb','gry']
                        if value[i] in ecl_data:
                            succesCard[i] = 'accepted'
                            isAccept += 1
                        else:
                            succesCard[i] = 'denied'


                if isAccept == 7:
                    self.AllAcceptCards.append(index)




            if len(succesCard) > 0:
                self.SuccesLoginCards.append(succesCard)






