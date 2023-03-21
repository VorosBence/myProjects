class AllowedCardsCheck():
    def __init__(self,db,allowed):
        self.db = db
        self.allowed = allowed

    def CardsOutPut(self):
        for index,value in enumerate(self.db):
            if index in self.allowed:
                for i in value:
                    if i == 'pid':
                        try:
                            int(value[i])
                            if len(value[i]) == 9:
                                print(f'ez kilenc {value[i]}')
                            else:
                                print(f'kevesebb vagy több mint {value[i]} {index}')
                        except:
                            continue





