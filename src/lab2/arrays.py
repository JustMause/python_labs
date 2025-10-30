a = [[1, 2], [3, 4]]
b = [[1, 2], (3, 4, 5)]
c = [[1], [], [2, 3]]
d = [[1, 2], "ab"]
def min_max(nums: list[float | int]) -> tuple[float | int, float | int]:
    if not nums:
        raise ValueError()
    return (min(nums), max(nums))

def unique_sorted(nums: list[float | int]) -> tuple[float | int, float | int]:
    return (sorted(set(nums)))

def flatten(mat: list[list | tuple]) -> list:
    mat2 = []
    for el in mat:
        if not isinstance(el, (list, tuple)):
            raise TypeError()

        mat2.extend(el)
    return(mat2)


print(flatten(a))
print(flatten(b))
print(flatten(c))
print(flatten(d))
