def matriX(a, b):
    # a = int(input('No of row: '))
    # b = int(input('No of column: '))
    k = 0
    matrix = []

    for i in range(a):
        row = []
        for j in range(b):
            try:
                row.append(int(input('enter each number in a row basis and only once at a time: ')))
            except ValueError:
                row.append(0)
        matrix.append(row)

    for i in range(a):
        for j in range(b):
            print(matrix[i][j], end=' ')
        print()

    return matrix


def size(data):
    for i in data:
        return f'row|column : {len(data)}|{len(i)}'


def vector(a, iterable):
    for i in range(a):
        print(iterable[i])
    print(f'row|column : {len(iterable)}|{1}')


vector(4, [2121, 2233, 3123, 23324])


def position(i, j, iterable):
    return iterable[i-1][j-1]


print(position(2, 3, matriX(2, 3)))


def multiply(major, minor):
    a = []
    b = 0
    for i in major:
        op = []
        for k in i:
            op.append(k * minor[b])
            b += 1
        a.append(sum(op))
        b = 0
    print(a)


multiply([[1, 2, 3], [4, 5, 6], [7, 8, 9]], [1, 1, 1])