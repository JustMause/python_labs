a = [3, -1, 5, 5, 0]
b = [3, 1, 2, 1, 3]
c = [[1, 2], [3, 4]]
mat2 = []
def min_max(nums: list[float | int]) -> tuple[float | int, float | int]:
    return (min(nums), max(nums))

def unique_sorted(nums: list[float | int]) -> tuple[float | int, float | int]:
    return (sorted(set(nums)))

def flatten(mat: list[list | tuple]) -> list:
    for el in mat:
        mat2.extend(el)
    return(mat2)


print(min_max(a))
print(unique_sorted(b))
print(flatten(c))