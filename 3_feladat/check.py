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



def convert_character(__string__= 'bence'):
    return [ord(char) for char in __string__]


def check_character(__list__ = convert_character()):
    print(len(ascii))

check_character()

character2 = []
for index, ans in enumerate(answers):
    for indexy,data in enumerate(ans):
        character2 = []
        
       
    



