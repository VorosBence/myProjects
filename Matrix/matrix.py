import random

matrix_size = 10
rows = []
sum_column = 0
sum_column_1 = []
sum_rows_1 = []
sum_even = []
sum_odd = []
matrix = []
for column in range(matrix_size):
    rows = []
    for row in range(matrix_size):
        rows.append(random.randint(10,99))
    matrix.append(rows)



def printMatrix():
    for nums in matrix:
        print(nums)

def allRows():
    for index in range(matrix_size):
        print(f'Row {index + 1} sum : {sum(matrix[index])}')
        sum_rows_1.append(sum(matrix[index]))
def allColumn():
    for index in range(matrix_size):
        sum_column = 0
        for i in range(matrix_size):
            sum_column += matrix[i][index]
        print(f'Column {index + 1} sum : {sum_column}')
        sum_column_1.append(sum_column)
def EvenOdd():
    for index in range(matrix_size):
        for number in matrix[index]:
            if number % 2 == 0:
                sum_even.append(number)
            else:
                sum_odd.append(number)





printMatrix()
allRows()
allColumn()
EvenOdd()

count = 0
with open('file.txt','w') as file:
    for index in range(matrix_size):
        if count == 0:
            file.write('[')
        for value in matrix[index]:
            count+=1
            file.write(f'{str(value)}, ')

        if count == matrix_size:
            count = 0
            file.write(']')
            file.write(f' Row {str(index+1)} sum : {str(sum_rows_1[index])}')
            file.write("\n")

    for index in range(matrix_size):
        file.write(f'Column {str(index+1)} sum : {str(sum_column_1[index])} \n')


    file.write('\n\n\n\n')
    file.write('Even Numbers\n')
    for index in sum_even:
        file.write(f'{str(index)} ')

    file.write(f'\nSum : {str(len(sum_even))}\n')
    file.write('\n\n')
    file.write('Odd Numbers\n')
    for index in sum_odd:
        file.write(f'{str(index)} ')

    file.write(f'\nSum : {str(len(sum_odd))}')