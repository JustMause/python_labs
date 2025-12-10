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

## Лабораторная работа 5

### Задание 1

import csv, json, sys, os

from pathlib import Path


def is_valid_json_file(file_path: str) -> bool:

    try:
    
        if not os.path.exists(file_path) or os.path.getsize(file_path) == 0:
        
            return False
            
        with open(file_path, 'r', encoding='utf-8') as file:
            json_data = json.load(file)
            
            return isinstance(json_data, list) and len(json_data) > 0 and all(isinstance(item, dict) for item in json_data)
            
    except:
    
        return False


def is_valid_csv_file(file_path: str) -> bool:

    try:
    
        if not os.path.exists(file_path) or os.path.getsize(file_path) == 0:
        
            return False

        with open(file_path, 'r', encoding='utf-8') as file:
        
            reader = csv.reader(file)
            
            header = next(reader, None)
            
            return header is not None and len(header) > 0
            
    except:
    
        return False


def json_to_csv(json_path: str, csv_path: str) -> None:

    if not is_valid_json_file(json_path):
    
        print("ValueError: Input file is not a valid JSON or is empty")
        
        sys.exit(1)
        
    json_path = Path(json_path)
    
    csv_path = Path(csv_path)
    
    if json_path.suffix.lower() != ".json":
    
        raise ValueError(f"Неверный формат входного файла: ожидается .json")
        
    if csv_path.suffix.lower() != ".csv":
    
        raise ValueError(f"Неверный формат выходного файла: ожидается .csv")

    with open(json_path, 'r', encoding='utf-8') as json_file:
    
        json_data = json.load(json_file)
        

    with open(csv_path, 'w', newline='', encoding='utf-8') as csvfile:
    
        writer = csv.DictWriter(csvfile, fieldnames=json_data[0].keys())
            
        writer.writeheader()
        
        writer.writerows(json_data)


def csv_to_json(csv_path: str, json_path: str) -> None:

    if not is_valid_csv_file(csv_path):
    
        print("ValueError: Input file is not a valid CSV or is empty")
        
        sys.exit(1)
        
    json_path = Path(json_path)
    
    csv_path = Path(csv_path)
    
    if json_path.suffix.lower() != ".json":
    
        raise ValueError(f"Неверный формат выходного файла: ожидается .json")
        
    if csv_path.suffix.lower() != ".csv":
    
        raise ValueError(f"Неверный формат входного файла: ожидается .csv")

    with open(csv_path, 'r', encoding='utf-8') as csvfile:
    
        reader = csv.DictReader(csvfile)
        
        data = list(reader)

    with open(json_path, 'w', encoding='utf-8') as jsonfile:
    
        json.dump(data, jsonfile, ensure_ascii=False, indent=4)


csv_to_json(r"C:\Users\Home\python_labs\data\samples\people.csv",
            r"C:\Users\Home\python_labs\data\out\people_from_csv.json")

json_to_csv(r"C:\Users\Home\python_labs\data\samples\people.json",
            r"C:\Users\Home\python_labs\data\out\people_from_json.csv")

![Image alt](https://github.com/JustMause/python_labs/raw/main/images/lab5/01_5.png)

![Image alt](https://github.com/JustMause/python_labs/raw/main/images/lab5/02_5.png)

![Image alt](https://github.com/JustMause/python_labs/raw/main/images/lab5/03_5.png)

![Image alt](https://github.com/JustMause/python_labs/raw/main/images/lab5/04_5.png)

### Задание 2

import os

import csv

import sys

from pathlib import Path

from openpyxl import Workbook

def csv_to_xlsx(csv_path: str, xlsx_path: str) -> None:

    if not os.path.exists(csv_path):
    
        print("FileNotFoundError")
        
        sys.exit(1)
        
    xlsx_path=Path(xlsx_path)
    
    csv_path=Path(csv_path)
    
    if xlsx_path.suffix.lower() != ".xlsx":
    
        raise ValueError(f"Неверный формат выходного файла: ожидается .xlsx")
        
    if csv_path.suffix.lower() != ".csv":
    
        raise ValueError(f"Неверный формат входного файла: ожидается .csv")

    if os.path.getsize(csv_path) == 0:
    
        print("ValueError")
        sys.exit(1)
        
    wb = Workbook()
    
    ws = wb.active
    
    ws.title = "Sheet1"

    with open(csv_path, "r", encoding="utf-8") as csv_file:
    
        reader = csv.reader(csv_file)
        
        for row in reader:
        
            ws.append(row)
            
    for column_cells in ws.columns:
        max_length = 0
        
        column_letter = column_cells[0].column_letter
        
        for cell in column_cells:
        
            if cell.value:
            
                max_length = max(max_length, len(str(cell.value)))
                
        ws.column_dimensions[column_letter].width = max(max_length + 2, 8)
    wb.save(xlsx_path)
    
csv_to_xlsx(r"C:\Users\Home\python_labs\data\samples\cities.csv", r"C:\Users\Home\python_labs\data\out\people.xlsx")

![Image alt](https://github.com/JustMause/python_labs/raw/main/images/lab5/05_5.png)

![Image alt](https://github.com/JustMause/python_labs/raw/main/images/lab5/06_5.png)

## Лабораторная работа 6

### Задание 1

import argparse

from pathlib import Path

from lib.text import normalize, tokenize, count_freq, top_n

def main():

    parser = argparse.ArgumentParser(description="CLI‑утилиты лабораторной №6")
    
    subparsers = parser.add_subparsers(dest="command")
    
    cat_parser = subparsers.add_parser("cat", help="Вывести содержимое файла")
    
    cat_parser.add_argument("--input", required=True)
    
    cat_parser.add_argument("-n", action="store_true", help="Нумеровать строки")
    
    stats_parser = subparsers.add_parser("stats", help="Частоты слов")
    
    stats_parser.add_argument("--input", required=True)
    
    stats_parser.add_argument("--top", type=int, default=5)
    
    args = parser.parse_args()
    
    file_path = Path(args.input)
    
    if not file_path.exists():
    
        parser.error(f"Файл '{args.input}' не найден")
        
    if args.command == "cat":
    
        try:
        
            with file_path.open("r", encoding="utf-8") as f:
            
                for i, line in enumerate(f, start=1):
                
                    line = line.rstrip("\n")
                    
                    if args.n:
                    
                        print(f"{i}: {line}")
                        
                    else:
                    
                        print(line)
                        
        except Exception as e:
        
            parser.error(f"Ошибка при чтении файла: {e}")
            
    elif args.command == "stats":
    
        try:
            with file_path.open("r", encoding="utf-8") as f:
            
                text = f.read()
                
                top_words = top_n(count_freq(tokenize(normalize(text))), args.top)
                
            if not top_words:
            
                print("Слова в файле не найдены")
                
                return
            print(f"Топ {args.top} слов:")
            
            for word, count in top_words:
            
                print(f"{word}: {count}")
                
        except Exception as e:
        
            parser.error(f"Ошибка при чтении файла: {e}")
            
    else:
    
        parser.print_help()
        
if __name__ == "__main__":

    main()

![Image alt](https://github.com/JustMause/python_labs/raw/main/images/lab6/01_6.jpg)

![Image alt](https://github.com/JustMause/python_labs/raw/main/images/lab6/02_6.jpg)

![Image alt](https://github.com/JustMause/python_labs/raw/main/images/lab6/03_6.png)

### Задание 2

import argparse

from lib.json_csv import *

from lib.csv_xlsx import *

def main():

    parser = argparse.ArgumentParser()
    
    sub = parser.add_subparsers(dest="cmd")

    # json → csv
    
    json2csv_parser = sub.add_parser("json2csv")
    
    json2csv_parser.add_argument("--in", dest="input", required=True, help="Путь к входному JSON")
    
    json2csv_parser.add_argument("--out", dest="output", required=True, help="Путь к выходному CSV")

    # csv → json
    
    csv2json_parser = sub.add_parser("csv2json")
    
    csv2json_parser.add_argument("--in", dest="input", required=True, help="Путь к входному CSV")
    
    csv2json_parser.add_argument("--out", dest="output", required=True, help="Путь к выходному JSON")

    # csv → xlsx
    
    csv2xlsx_parser = sub.add_parser("csv2xlsx")
    
    csv2xlsx_parser.add_argument("--in", dest="input", required=True, help="Путь к входному CSV")
    
    csv2xlsx_parser.add_argument("--out", dest="output", required=True, help="Путь к выходному XLSX")

    args = parser.parse_args()

    input_path = Path(args.input)
    
    if not input_path.exists():
    
        parser.error(f"Входной файл '{args.input}' не найден")

    if args.cmd == "json2csv":
    
        json_to_csv(args.input, args.output)
        
    elif args.cmd == "csv2json":
    
        csv_to_json(args.input, args.output)
        
    elif args.cmd == "csv2xlsx":
    
        csv_to_xlsx(args.input, args.output)
        
    else:
        parser.print_help()
        


if __name__ == "__main__":

    main()
    
![Image alt](https://github.com/JustMause/python_labs/raw/main/images/lab6/04_6.png)

![Image alt](https://github.com/JustMause/python_labs/raw/main/images/lab6/05_6.png)

![Image alt](https://github.com/JustMause/python_labs/raw/main/images/lab6/06_6.png)
