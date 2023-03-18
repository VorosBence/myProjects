import random

class Matrix:

    def __init__(self,size):
        self.matrix_size = size
        self.rows = []
        self.sum_column_1 = []
        self.sum_rows_1 = []
        self.sum_even = []
        self.sum_odd = []
        self.matrix = []

    def createMatrix(self):
        for column in range(self.matrix_size):
            self.rows = []
            for row in range(self.matrix_size):
                self.rows.append(random.randint(10, 99))
            self.matrix.append(self.rows)

    def printMatrix(self):
        for nums in self.matrix:
            print(nums)

    def allRows(self):
        for index in range(self.matrix_size):
            print(f'Row {index + 1} sum : {sum(self.matrix[index])}')
            self.sum_rows_1.append(sum(self.matrix[index]))

    def allColumn(self):
        for index in range(self.matrix_size):
            sum_column = 0
            for i in range(self.matrix_size):
                sum_column += self.matrix[i][index]
            print(f'Column {index + 1} sum : {sum_column}')
            self.sum_column_1.append(sum_column)

    def EvenOdd(self):
        for index in range(self.matrix_size):
            for number in self.matrix[index]:
                if number % 2 == 0:
                    self.sum_even.append(number)
                else:
                    self.sum_odd.append(number)

        return self.sum_even, self.sum_odd


    def exportFile(self,name):
        count = 0
        if name.endswith(".txt"):
            filename = name
        elif name == '':
            filename = 'MatrixFile.txt'
        else:
            filename = f'{name}.txt'

        with open(filename, 'w') as file:
            for index in range(self.matrix_size):
                if count == 0:
                    file.write('[')
                for value in self.matrix[index]:
                    count += 1
                    file.write(f'{str(value)}, ')

                if count == self.matrix_size:
                    count = 0
                    file.write(']')
                    file.write(f' Row {str(index + 1)} sum : {str(self.sum_rows_1[index])}')
                    file.write("\n")

            for index in range(self.matrix_size):
                file.write(f'Column {str(index + 1)} sum : {str(self.sum_column_1[index])} \n')

            file.write('\n\n\n\n')
            file.write('Even Numbers\n')
            for index in self.sum_even:
                file.write(f'{str(index)} ')

            file.write(f'\nSum : {str(len(self.sum_even))}\n')
            file.write('\n\n')
            file.write('Odd Numbers\n')
            for index in self.sum_odd:
                file.write(f'{str(index)} ')

            file.write(f'\nSum : {str(len(self.sum_odd))}')
m1= Matrix(4)
m1.createMatrix()
m1.printMatrix()
m1.allRows()
m1.allColumn()
print(m1.EvenOdd())
m1.exportFile('')