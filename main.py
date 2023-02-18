import openpyxl
import random
'''workbook = openpyxl.load_workbook('valami.xlsx')
worksheet = workbook['Munka1']

Datas = []
data = {}
for row in worksheet.iter_rows(min_row=2, values_only=True):
    data = {}
    data['Id'] = row[1]
    data['Name'] = row[2]
    data['Position'] = row[3]
    data['Supervisor'] = row[4]
    data['Start'] = str(row[5])
    data['Benefits'] = row[6]

    Datas.append(data)
'''
book = openpyxl.Workbook()
sheet = book.active

sheet['B1'] = 'Id'
sheet['C1'] = 'Name'
sheet['D1'] = 'Position'
sheet['E1'] = 'Supervisor'
sheet['F1'] = 'Start'
sheet['G1'] = 'Benefits'

for id in range(0,50):

    id_sheet = 'B'+str(id+2)
    sheet[id_sheet] = id+2

book.save('test.xlsx')

position = {1:'Owner',2:'DepartmentLeader',3:'Teamleader',4:'Developer'}
position_list = []
benefits = {1:'Car',2:'Phone',3:'Fuel card',4:'Gift card'}
def generate(max_num):
    position_line_data = {}
    position_line_data['Id'] = 2
    position_line_data['Name'] = 'Voros Bence'
    position_line_data['Position'] = position[1]
    position_line_data['Supervisor'] = None
    position_line_data['Start'] = '2010.10.11'
    position_line_data['Benefits'] = benefits[random.randint(1,4)]
    position_list.append(position_line_data)

    DL = round((max_num/100)*20)
    TL = round((max_num/100)*30)
    Dev = max_num-(DL+TL)

    for id in range(1,max_num):
        position_line_data = {}
        position_line_data['Id'] = id+2

    print(position_list)

generate(50)








