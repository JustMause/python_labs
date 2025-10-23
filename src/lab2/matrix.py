def transpose(mat: list[list[float | int]]) -> list[list]:
    if not mat:
        return []
    row_length = len(mat[0])
    for row in mat:
        if len(row) != row_length:
            raise ValueError()
    transposed = []
    for col_index in range(len(mat[0])):
        new_row = []
        for row in mat:
            new_row.append(row[col_index])
        transposed.append(new_row) 
    return transposed

def row_sums(mat: list[list[float | int]]) -> list[float]:
    if not mat:
        return []
    if mat:
        row_length = len(mat[0])
        for row in mat:
            if len(row) != row_length:
                raise ValueError()
    sums = []
    for row in mat:
        row_sum = sum(row)
        sums.append(row_sum)
    return sums


def col_sums(mat: list[list[float | int]]) -> list[float]:
    if not mat:
        return []
    if mat:
        row_length = len(mat[0])
        for row in mat:
            if len(row) != row_length:
                raise ValueError()
    transposed = transpose(mat)
    sums = []
    for col in transposed:
        col_sum = sum(col)
        sums.append(col_sum)   
    return sums
