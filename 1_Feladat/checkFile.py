def checkFiles(db):
    AllIndexReturn = []
    AllDniedIndexReturn = []
    for index,data in enumerate(db):
        checkValue = 0
        for id in data:
            if id == 'pid' or id == 'byr' or id == 'iyr' or id == 'eyr' or id == 'hgt' or id == 'hcl' or id == 'ecl':
                checkValue += 1
        if checkValue == 7:
            AllIndexReturn.append(index)
        else:
            AllDniedIndexReturn.append(index)
    return AllIndexReturn,AllDniedIndexReturn, len(AllIndexReturn),len(AllDniedIndexReturn)
def checkId(db,AllIndex):
    allowed = []
    rejected = []
    for index,data in enumerate(db):
        if index in AllIndex:
            accept = 0
            denied = 0
            for id in data:
                key = data[id]
                if id == 'pid':

                    try:
                        int(key)
                        if len(key) == 9:
                            accept += 1
                        else:
                            denied += 1
                    except:
                        denied += 1
                if id == 'byr':
                    if len(str(key)) == 4 and 1920 < int(key) < 2002:
                        accept += 1
                    else:
                        denied += 1
                if id == 'iyr':
                    if len(str(key)) == 4 and 2010 < int(key) < 2021:
                        accept += 1
                    else:
                        denied += 1
                if id == 'eyr':
                    if len(str(key)) == 4 and 2021 < int(key) < 2031:
                        accept += 1
                    else:
                        denied += 1
                if id == 'hgt':
                    if key[-2:] == 'cm' and 50 < int(key[:-2]) < 220:
                        accept += 1
                    elif key[-2:] == 'in' and 20 < int(key[:-2]) < 90:
                        accept += 1
                    else:
                        denied += 1
                if id == 'hcl':
                    hashtag = key[:1]
                    color = key[1:]
                    color_alphabets = ['a', 'b', 'c', 'd', 'e', 'f']
                    color_nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
                    colorCheck = 0
                    if hashtag == '#':
                        for color_index in range(6):
                            if color[color_index] in color_alphabets or int(color[color_index]) in color_nums:
                                colorCheck += 1
                    if colorCheck == 6:
                        accept += 1
                    else:
                        denied += 1
                if id == 'ecl':
                    ecl_data = ['grn', 'blu', 'brn', 'hzl', 'oth', 'amb', 'gry']
                    if key in ecl_data:
                        accept += 1
                    else:
                        denied += 1
            if accept == 7:
                allowed.append(index)
            else:
                rejected.append(index)

    return allowed,rejected,len(allowed),len(rejected)