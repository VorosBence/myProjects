class loginReturn():
    def __init__(self,db):
        self.db = db

    def argsCheck(self):
        pid = False
        byr = False
        cid = False
        iyr = False
        eyr = False
        hgt = False
        hcl = False
        ecl = False
        for line in self.db:
            for data in line:
                if data == 'pid':
                    pid = True
                elif data == 'byr':
                    byr = True
                elif data == 'cid':
                    cid = True
                elif data == 'iyr':
                    iyr = True
                elif data == 'eyr':
                    eyr = True
                elif data == 'hgt':
                    hgt = True
                elif data == 'hcl':
                    hcl = True
                elif data == 'ecl':
                    ecl = True

