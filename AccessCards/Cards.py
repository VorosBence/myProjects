class cardsData:
    def __init__(self):
        self.database = []
        self.temp_database = []
    def readFile(self):
        temp_data = []
        with open('cardsData.txt','r') as file:
            for line in file:
                data_line = line.strip().split()
                if len(data_line) > 0:
                    for data in data_line:
                        temp_data.append(data)
                else:
                    self.temp_database.append(temp_data)
                    temp_data = []
        datas = {}
        for lines in self.temp_database:
            for data in lines:
                colon = data.find(':')
                datas[data[:colon]] = data[colon+1:]

            self.database.append(datas)
            datas = {}
    def print_temp_data(self):
        for data in self.temp_database:
            print(data)
    def printDB(self):
        for data in self.database:
            print(data)