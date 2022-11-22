import copy

class Matrix():
    def __init__(self, list_matr):
        self.list_matr = list_matr

    def __str__(self):
        matrix = ''
        for i in range(len(self.list_matr)):
            matrix = matrix + '  '.join(map(str, self.list_matr[i])) + '\n'
        return matrix

    def __add__(self, other):
        sum_matrix = copy.deepcopy(self.list_matr)
        for i in range(len(self.list_matr)):
            for j in range(len(self.list_matr[i])):
                sum_matrix[i][j] = self.list_matr[i][j] + other.list_matr[i][j]
        return Matrix(sum_matrix)


a = Matrix([[1, 2, 3], [2, 3, 5], [5, 4, 2]])
print(a)
b = Matrix([[7, 2, 5], [8, 3, 9], [7, 6, 9]])
print(b)
print(a + b)