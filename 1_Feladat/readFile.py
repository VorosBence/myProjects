def read_file(filename):
    database = []
    temp_data = []
    with open(filename, 'r') as file:
        for line in file:
            data_line = line.strip().split()
            if data_line:
                temp_data.extend(data_line)
            else:
                datas = {}
                for data in temp_data:
                    colon = data.find(':')
                    key = data[:colon]
                    value = data[colon + 1:]
                    datas[key] = value
                database.append(datas)
                temp_data = []
    return database