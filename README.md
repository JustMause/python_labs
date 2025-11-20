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

## Лабораторная работа 3

### Задание 1

import re


def normalize(text: str, *, casefold: bool = True, yo2e: bool = True) -> str:

    if not text:
    
        return ""
        
    result = text
    
    if casefold:
    
        result = result.casefold()
        
    if yo2e:
    
        result = result.replace('ё', 'е').replace('Ё', 'Е')
        
    special_simvols = ['\t', '\r', '\n']
    
    for simvol in special_simvols:
    
        result = result.replace(simvol, ' ')
        
    result = ' '.join(result.split())

    return result

def tokenize(text: str) -> list[str]:

    if not text:
    
        return []
        
    pattern = r'\w+(?:-\w+)*'
    
    tokens = re.findall(pattern, text)
    
    return tokens

def count_freq(tokens: list[str]) -> dict[str, int]:

    freq_dict = {}
    
    for token in tokens:
    
        freq_dict[token] = freq_dict.get(token, 0) + 1

    return freq_dict

def top_n(freq: dict[str, int], n: int = 5) -> list[tuple[str, int]]:

    if not freq:
    
        return []
        
    sorted_items = sorted(freq.items(),key=lambda x: (-x[1], x[0]))
    
    return sorted_items[:n]

![Image alt](https://github.com/JustMause/python_labs/raw/main/images/lab3/01_3.png)

![Image alt](https://github.com/JustMause/python_labs/raw/main/images/lab3/02_3.png)

![Image alt](https://github.com/JustMause/python_labs/raw/main/images/lab3/03_3.png)

### Задание 2

from lib.text import normalize, tokenize, count_freq, top_n

import sys


def main():

    text = sys.stdin.buffer.read().decode('utf-8')
    
    if not text.strip():
    
        print("Нет входных данных")
        
        return
        
    normalized_text = normalize(text)
    
    tokens = tokenize(normalized_text)
    

    if not tokens:
    
        print("В тексте не найдено слов")
        
        return

    total_words = len(tokens)
    
    freq_dict = count_freq(tokens)
    
    unique_words = len(freq_dict)
    
    top_words = top_n(freq_dict, 5)

    print(f"Всего слов: {total_words}")
    
    print(f"Уникальных слов: {unique_words}")
    
    print("Топ-5:")
    
    for word, count in top_words:
    
        print(f"{word}: {count}")


if __name__ == "__main__":

    main()
    
![Image alt](https://github.com/JustMause/python_labs/raw/main/images/lab3/04_3.png)
    
## Лабораторная работа 4

### Задание 1

import csv

from pathlib import Path

from typing import Iterable, Sequence

def read_text(path: str | Path, encoding: str = "utf-8") -> str:
    try:
    
        return Path(path).read_text(encoding=encoding)
        
    except FileNotFoundError:
    
        return "Такого файла нету"
        
    except UnicodeDecodeError:
    
        return "Неудалось изменить кодировку"

def write_csv(rows: list[tuple | list], path: str | Path, header: tuple[str, ...] | None = None) -> None:

    p = Path(path)
    
    with p.open('w', newline="", encoding="utf-8") as file:
    
        f = csv.writer(file)
        
        if header is None and rows == []:
        
            f.writerow(('a', 'b'))
            
        if header is not None:
        
            f.writerow(header)
            
        if rows != []:
        
            const = len(rows[0])
            
            for i in rows:
            
                if len(i) != const:
                
                    return ValueError
                    
        f.writerows(rows)

def ensure_parent_dir(path: str | Path) -> None:

    Path(path).parent.mkdir(parents=True, exist_ok=True)


![Image alt](https://github.com/JustMause/python_labs/raw/main/images/lab4/02_4.png)

### Задание 2

from io_txt_csv import read_text, write_csv, ensure_parent_dir

import sys

from pathlib import Path

from text import normalize, tokenize, count_freq, top_n


sys.path.append(r'C:\Users\Home\Documents\GitHub\src\lib')



def exist_path(path_f: str):

    return Path(path_f).exists()


def main(file: str, encoding: str = 'utf-8'):

    if not exist_path(file):
    
        raise FileNotFoundError

    file_path = Path(file)
    
    text = read_text(file, encoding=encoding)
    
    norm = normalize(text)
    
    tokens = tokenize(norm)
    
    freq_dict = count_freq(tokens)
    
    top = top_n(freq_dict, 5)
    
    top_sort = sorted(top, key=lambda x: (x[1], x[0]),
                      reverse=True)
                      
    report_path = file_path.parent / 'report.csv'
    
    write_csv(top_sort, report_path, header=('word', 'count'))

    print(f'Всего слов: {len(tokens)}')
    
    print(f'Уникальных слов: {len(freq_dict)}')
    
    print('Топ-5:')
    
    for cursor in top_sort:
    
        print(f'{cursor[0]}: {cursor[-1]}')


![Image alt](https://github.com/JustMause/python_labs/raw/main/images/lab4/04_4.png)
