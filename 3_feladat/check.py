answers = []
group = []
allowed = []
characters = 'abcdefghijklmnopqrstuvwxyz'
ascii = [ord(char) for char in characters]
with open('feladat3.txt','r') as file:
    for line in file:
        data = line.strip().split()
        if len(data) == 0:
            normal_group = [i for d in group for i in d]
            answers.append(normal_group)
            group = []
        else:
            group.append(data)



def convert_character(__string__):
    return list(set([ord(char) for char in __string__]))
def check_character(__list__):
    return len(characters) == len(__list__)

    
    




if check_character(convert_character(characters)):
    allowed.append(1)
else:
    allowed.append(2)



for index, ans in enumerate(answers):
    temp = ''
    for indexy,data in enumerate(ans):
        temp += data
    if check_character(convert_character(temp)):
        allowed.append((index))


print('Itt vannak azok a csoportok ahol az összes válasz szerepelt')
for i in allowed:  
    print(f'Index: {i}, {answers[i]}')