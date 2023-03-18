class cardsData:
    def __init__(self):
        self.database = []
        self.temp_database = []
        self.datas = {}

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



        for lines in self.temp_database:
            for data in lines:
                colon = data.find(':')
                self.datas[data[:colon]] = data[colon+1:]

            self.database.append(self.datas)
            self.datas = {}




            '''for data in data_line:

                    colon = data.find(':')
                    self.datas[data[:colon]] = data[colon+1:]
                    self.database.append(self.datas)
                    if len(data_line) > 0:
                        print(data_line)
                    else:
                        print('----')'''


    def print_temp_data(self):
        for data in self.temp_database:
            print(data)


    def printDB(self):
        for data in self.database:
            print(data)



c1 = cardsData()
c1.readFile()
#c1.print_temp_data()
c1.printDB()