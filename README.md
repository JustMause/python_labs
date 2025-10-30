# python_labs

## Лабораторная работа 1

### Задание 1

name = input()

age = int(input())

print(f'Привет, {name}! Через год тебе будет {age+1}.')

![Image alt](https://github.com/JustMause/python_labs/raw/main/images/lab1/01.png)

### Задание 2

a = float(input().replace(',','.'))

b = float(input().replace(',','.'))

sum = a+b

avg = (a+b)/2

print(f'sum = {sum:.2F}, avg = {avg:.2F}')

![Image alt](https://github.com/JustMause/python_labs/raw/main/images/lab1/02.png)

### Задание 3

price = float(input())

discount = float(input())

vat = float(input())

base = price * (1 - discount/100)

vat_amount = base * (vat/100)

total = base + vat_amount

print(f'База после скидки: {base:.2F} ₽')

print(f'НДС: {vat_amount:.2F} ₽')

print(f'Итого к оплате: {total:.2F} ₽')

![Image alt](https://github.com/JustMause/python_labs/raw/main/images/lab1/03.png)

### Задание 4

m = int(input())

hours = m // 60

min = m % 60

print(f"{hours}:{min:02d}")

![Image alt](https://github.com/JustMause/python_labs/raw/main/images/lab1/04.png)

### Задание 5

FIO = input().split()

F = FIO[0]

I = FIO[1]

O = FIO[2]

In = F[0]+I[0]+O[0]

sum = (len(F)+len(I)+len(O))+2

print(In,sum)

![Image alt](https://github.com/JustMause/python_labs/raw/main/images/lab1/05.png)


## Лабораторная работа 2

### Задание 1

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

![Image alt](https://github.com/JustMause/python_labs/raw/main/images/lab2/01_2.png)

![Image alt](https://github.com/JustMause/python_labs/raw/main/images/lab2/02_2.png)

![Image alt](https://github.com/JustMause/python_labs/raw/main/images/lab2/03_2.png)

### Задание 2

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
    
![Image alt](https://github.com/JustMause/python_labs/raw/main/images/lab2/04_2.png)

![Image alt](https://github.com/JustMause/python_labs/raw/main/images/lab2/05_2.png)

![Image alt](https://github.com/JustMause/python_labs/raw/main/images/lab2/06_2.png)

### Задание 3

a = ("Иванов Иван Иванович", "BIVT-25", 4.6)

def format_record(rec):

    fio, group, gpa = rec
    
    if not fio or not group:
    
        raise ValueError()
    
    if not isinstance(gpa, (int, float)):
    
        raise TypeError()
    
    fio_parts = fio.split()
    
    fio_clean = []
    
    for part in fio_parts:
    
        if part.strip():
        
            fio_clean.append(part.strip())
    
    if len(fio_clean) < 2:
    
        raise ValueError()
    
    surname = fio_clean[0]
    
    initials = ""
    
    for i in range(1, len(fio_clean)):
    
        if fio_clean[i]:
        
            initials += fio_clean[i][0].upper() + "."
    
    formatted_fio = surname.capitalize() + " " + initials
    
    formatted_gpa = f"{gpa:.2f}"
    
    return f"{formatted_fio}, гр. {group}, GPA {formatted_gpa}"

![Image alt](https://github.com/JustMause/python_labs/raw/main/images/lab2/07_2.png)
