
class cardsData:
    def __init__(self):
        self.database = []
        self.datas = {}

    def readFile(self):
        with open('cardsData.txt','r') as file:
            for line in file:
                data_line = line.strip().split()
                #print(len(data_line))

                if len(data_line) > 0:
                    for i in data_line:
                        print(i)
                        print(i.find(':'))
                        colon = i.find(':')
                        print(i[:colon])
                        print(i[colon+1:])

                elif len(data_line) == 0:
                    print('----')
                '''if len(data_line) == 0:
                    print('----')
                else:
                    print(data_line)
'''
c1 = cardsData()
c1.readFile()