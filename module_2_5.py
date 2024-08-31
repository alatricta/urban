def get_matrix(n: int, m: int, value):
    matrix = []
    for i in range(n):
        matrix.append([])
        for j in range(m):
            matrix[i].append(value)
    return Matrix(matrix)


class Matrix:
    def __init__(self, m: list):
        self.m = m

    def __str__(self):
        text = ''
        for line in self.m:
            text += str(line) + '\n'
        return text


if __name__ == '__main__':
    mt: Matrix = get_matrix(3,2,10)
    print(mt)
