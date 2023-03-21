class loginReturn():
    def __init__(self,db):
        self.db = db
        self.log = []
        self.errors = []
        self.okLogCard = []
    def argsCheck(self):
        for key,line in enumerate(self.db):
            pid = False
            byr = False
            cid = False
            iyr = False
            eyr = False
            hgt = False
            hcl = False
            ecl = False
            for data in line:
                checkBook = {}
                if data == 'pid':
                    pid = True
                if data == 'byr':
                    byr = True
                if data == 'cid':
                    cid = True
                if data == 'iyr':
                    iyr = True
                if data == 'eyr':
                    eyr = True
                if data == 'hgt':
                    hgt = True
                if data == 'hcl':
                    hcl = True
                if data == 'ecl':
                    ecl = True

            checkBook['pid'] = pid
            checkBook['byr'] = byr
            checkBook['cid'] = cid
            checkBook['iyr'] = iyr
            checkBook['eyr'] = eyr
            checkBook['hgt'] = hgt
            checkBook['hcl'] = hcl
            checkBook['ecl'] = ecl
            self.log.append(checkBook)

    def searchError(self):
        for index,line in enumerate(self.log):
            error = {}
            for id,data in enumerate(line):
                if line[data] == True:
                    error['Index'] = index
                else:
                    error[id] = data
            self.errors.append(error)

    def loginCardsOK(self):
        self.allowed = 0 #len
        self.Denied = [] #indexek
        self.denied = 0 #len
        for i in self.errors:
            logOk = {}
            for index in i:
                logOk['ID'] = i['Index']
                if index == 'Index':
                    continue
                elif i[index] != 'cid':
                    logOk['OK'] = 'no'
                    if i['Index'] not in self.Denied:
                        self.Denied.append(i['Index'])

                else:
                    logOk['OK'] = 'yes'
            self.okLogCard.append(logOk)
        self.allowed = len(self.db) - len(self.Denied)
        self.denied = len(self.Denied)


