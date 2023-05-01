answers = []
group = []
allowed = []
characters = 'abcdefghijklmnopqrstuvwxyz'
with open('feladat3.txt','r') as file:
    for line in file:
        data = line.strip().split()
        if len(data) == 0:
            normal_group = [i for d in group for i in d]
            answers.append(normal_group)
            group = []
        else:
            group.append(data)

character2 = []
for index, ans in enumerate(answers):
    for indexy,data in enumerate(ans):
        character2 = []
        character2.append(d for d in data if not character2)
        print(index,character2)
    





