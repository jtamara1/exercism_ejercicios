class Matrix:
    def __init__(self, matrix_string):
        self.m = [[int(y) for y in x.split()] for x in matrix_string.split("\n")]

    def row(self, index):
        index = index-1
        return self.m[index]

    def column(self, index):
        index = index-1
        return [self.m[x][index] for x in range(len(self.m))]
