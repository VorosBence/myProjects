class loginReturn():
    def __init__(self,db):
        self.db = db
        self.log = []
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
            checkBook['ID'] = key
            checkBook['pid'] = pid
            checkBook['byr'] = byr
            checkBook['cid'] = cid
            checkBook['iyr'] = iyr
            checkBook['eyr'] = eyr
            checkBook['hgt'] = hgt
            checkBook['hcl'] = hcl
            checkBook['ecl'] = ecl
            self.log.append(checkBook)

