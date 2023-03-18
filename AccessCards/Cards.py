
class cardsData:
    def __init__(self):
        self.database = []
        self.datas = {}

    def readFile(self):
        with open('cardsData.txt','r') as file:
            for line in file:
                data_line = line.strip().split()
                if len(data_line) > 0:
                    for data in data_line:
                        colon = data.find(':')
                        self.datas[data[:colon]] = data[colon+1:]
                        self.database.append(self.datas)
                else:
                    self.datas = {}


c1 = cardsData()
c1.readFile()
print(c1.database)