a = []
b = []
c = []

def transpose(mat: list[list[float | int]]) -> list[list]:
    num_cols = len(mat[0])
    if any(len(row) != num_cols for row in mat):
        raise ValueError()
    return [[mat[i][j] for i in range(len(mat))] for j in range(len(mat[0]))]

print(transpose(a))


def row_sums(mat: list[list[float | int]]) -> list[float]:
    
    if mat and any(len(row) != len(mat[0]) for row in mat):
        raise ValueError()
    
    return [float(sum(row)) for row in mat]

print(row_sums(b))

def col_sums(mat: list[list[float | int]]) -> list[float]:

    if not mat:
        return []
    

    if mat and any(len(row) != len(mat[0]) for row in mat):
        raise ValueError()
    
    if not mat[0]:
        return []
    
    return [float(sum(mat[i][j] for i in range(len(mat)))) for j in range(len(mat[0]))]

print(col_sums(c))
