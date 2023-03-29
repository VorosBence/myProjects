def readFile():
    with open('feladat2.txt', 'r') as file:
        database = []
        for line in file:
            data_line = line.strip().split()
            database.append(data_line)
    return database