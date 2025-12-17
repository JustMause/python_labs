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

## Лабораторная работа 7

### Задание 1 (text.py)

import pytest

from src.text import normalize, tokenize, count_freq, top_n


@pytest.mark.parametrize(

    "source, expected",
    
    [
    
        ("ПрИвЕт\nМИр\t", "привет мир"),
        
        ("ёжик, Ёлка", "ежик, елка"),
        
        ("Hello\r\nWorld", "hello world"),
        
        ("  двойные   пробелы  ", "двойные пробелы"),
        
        ("", ""),
        
        ("   ", ""),
        
    ],
)
def test_normalize(source, expected):

    assert normalize(source) == expected


@pytest.mark.parametrize(

    "text, expected",
    [
        ("привет мир", ["привет", "мир"]),
        
        ("hello world test", ["hello", "world", "test"]),
        
        ("", []),
        
        ("   ", []),
        
        ("знаки, препинания! тест.", ["знаки", "препинания", "тест"]),
        
    ],
    
)
def test_tokenize(text, expected):

    assert tokenize(text) == expected
    


def test_count_freq_basic():

    tokens = ["apple", "banana", "apple", "cherry", "banana", "apple"]
    
    result = count_freq(tokens)
    
    expected = {"apple": 3, "banana": 2, "cherry": 1}
    
    assert result == expected


def test_count_freq_empty():

    assert count_freq([]) == {}


def test_top_n_basic():

    freq = {"apple": 5, "banana": 3, "cherry": 7, "date": 1}
    
    result = top_n(freq, 2)
    
    expected = [("cherry", 7), ("apple", 5)]
    
    assert result == expected


def test_top_n_tie_breaker():

    freq = {"banana": 3, "apple": 3, "cherry": 3}
    
    result = top_n(freq, 3)
    
    expected = [("apple", 3), ("banana", 3), ("cherry", 3)]
    
    assert result == expected


def test_top_n_empty():

    assert top_n({}, 5) == []


def test_full_pipeline():

    text = "Привет мир! Привет всем. Мир прекрасен."
    
    normalized = normalize(text)
    
    tokens = tokenize(normalized)
    
    freq = count_freq(tokens)
    
    top_words = top_n(freq, 2)

    assert normalized == "привет мир! привет всем. мир прекрасен."
    
    assert tokens == [
    
        "привет",
        
        "мир",
        
        "привет",
        
        "всем",
        
        "мир",
        
        "прекрасен",
        
    ]
    assert freq == {"привет": 2, "мир": 2, "всем": 1, "прекрасен": 1}
    
    assert top_words == [("мир", 2), ("привет", 2)]

 ### Задание 2 (json_csv.py)

import pytest

import json

import csv

from src.json_csv import json_to_csv, csv_to_json


#JSON→CSV

@pytest.mark.parametrize(

    "test_name,data,expected_count",
    
    [
        ("basic", [{"name": "Alice", "age": 25}, {"name": "Bob", "age": 30}], 2),
        
        (
            "complex_data",

            [{"name": "Alice", "age": 25, "active": True, "score": 95.5}],
            
            1,
            
        ),
        
        (
            "different_order",
            
            [{"name": "Alice", "age": 25}, {"age": 30, "name": "Bob"}],
            2,
            
        ),
        ("empty_values", [{"name": "Alice", "age": 25, "comment": ""}], 1),
        
        ("unicode", [{"name": "Алиса", "message": "Привет! 🌍"}], 1),
    ],
)
JSON→CSV

def test_json_to_csv_success(tmp_path, test_name, data, expected_count):

    """параметризованный тест успешных преобразований JSON в CSV"""
    
    src = tmp_path / f"{test_name}.json"
    
    dst = tmp_path / f"{test_name}.csv"

    src.write_text(json.dumps(data, ensure_ascii=False), encoding="utf-8")
    
    json_to_csv(str(src), str(dst))

    assert dst.exists() #проверка_создания_файла
    
    with dst.open(encoding="utf-8") as f:
    
        rows = list(csv.DictReader(f))

    assert len(rows) == expected_count
    
    assert rows[0]["name"] == data[0]["name"]


@pytest.mark.parametrize(

    "test_name,csv_content,expected_count",
    [
        ("basic", "name,age\nAlice,25\nBob,30", 2),
        
        ("special_chars", 'name,description\n"Alice","Test, comma"', 1),
        
        ("semicolon_delim", "name;age\nAlice;25\nBob;30", 2),
    ],
)
def test_csv_to_json_success(tmp_path, test_name, csv_content, expected_count):

    """Параметризованный тест успешных преобразований CSV в JSON"""
    
    src = tmp_path / f"{test_name}.csv" 
    
    dst = tmp_path / f"{test_name}.json" 

    src.write_text(csv_content, encoding="utf-8")
    
    csv_to_json(str(src), str(dst))

    assert dst.exists()
    
    with dst.open(encoding="utf-8") as f:
    
        data = json.load(f)  #загрузка_json

    assert len(data) == expected_count


@pytest.mark.parametrize(

    "test_name,file_content,expected_error",
    [
        ("file_not_found", None, FileNotFoundError),
        
        ("invalid_json", "{ invalid json }", ValueError),
        
        ("empty_file", "", ValueError),
        
        ("not_list", '{"name": "test"}', ValueError),
        
        ("empty_list", "[]", ValueError),
        
        ("mixed_list", '[{"name": "test"}, "not_dict"]', ValueError),
        
        ("invalid_encoding", b"\xff\xfe\x00\x00", ValueError),
    ],
)

def test_json_to_csv_errors(tmp_path, test_name, file_content, expected_error):

    """Параметризованный тест ошибок JSON в CSV"""
    
    src = tmp_path / f"{test_name}.json"
    
    dst = tmp_path / "output.csv"

    if file_content is None:
    
        with pytest.raises(expected_error):
        
            json_to_csv("nonexistent.json", str(dst))
            
    else: 
    
        if isinstance(file_content, bytes):
        
            src.write_bytes(file_content)
            
        else:
        
            src.write_text(file_content, encoding="utf-8")
            

        with pytest.raises(expected_error):
        
            json_to_csv(str(src), str(dst))


@pytest.mark.parametrize(

    "test_name,file_content,expected_error",
    [
        ("file_not_found", None, FileNotFoundError),
        
        ("empty_file", "", ValueError),
        
        ("empty_header", "\nAlice,25", ValueError),
        
        ("empty_columns", "name,,age\nAlice,25,30", ValueError),
        
        ("invalid_encoding", b"\xff\xfe\x00\x00", ValueError),
    ],
)
def test_csv_to_json_errors(tmp_path, test_name, file_content, expected_error):

    """Параметризованный тест ошибок CSV в JSON"""
    
    src = tmp_path / f"{test_name}.csv"
    
    dst = tmp_path / "output.json"
    

    if file_content is None:
    
        with pytest.raises(expected_error):
        
            csv_to_json("nonexistent.csv", str(dst))
            
    else:
    
        if isinstance(file_content, bytes):
        
            src.write_bytes(file_content)
            
        else:
        
            src.write_text(file_content, encoding="utf-8")

        with pytest.raises(expected_error):
        
            csv_to_json(str(src), str(dst))


def test_json_csv_roundtrip(tmp_path):

    """Тест полного цикла преобразования"""
    
    original_json = tmp_path / "original.json"
    
    intermediate_csv = tmp_path / "intermediate.csv"
    
    final_json = tmp_path / "final.json"

    original_data = [{"name": "Alice", "age": 25}, {"name": "Bob", "age": 30}]
    
    original_json.write_text(json.dumps(original_data), encoding="utf-8")
    

    json_to_csv(str(original_json), str(intermediate_csv))
    
    csv_to_json(str(intermediate_csv), str(final_json))
    

    with final_json.open(encoding="utf-8") as f:
    
        final_data = json.load(f) 
        
    assert len(final_data) == 2 
    
    assert final_data[0]["name"] == "Alice"


def test_unexpected_errors(monkeypatch, tmp_path):

    """Тест неожиданных ошибок"""
    
    # Тест для JSON
    
    src_json = tmp_path / "test.json"
    
    dst_json = tmp_path / "test.csv"
    
    src_json.write_text('[{"name": "test"}]', encoding="utf-8")

    def mock_getsize(path):
    
        raise RuntimeError("Unexpected error")

    monkeypatch.setattr("os.path.getsize", mock_getsize) 
    
    with pytest.raises(ValueError, match="Неожиданная ошибка"):
    
        json_to_csv(str(src_json), str(dst_json))

    # Тест для CSV 
    
    src_csv = tmp_path / "test.csv"
    
    dst_csv = tmp_path / "test.json"
    
    src_csv.write_text("name,age\nAlice,25", encoding="utf-8")
    
    original_open = open

    def mock_open(*args, **kwargs):

        if args[0].endswith(".csv") and "r" in args[1]:
        
            raise RuntimeError("Unexpected read error")
            
        return original_open(*args, **kwargs)

    monkeypatch.setattr("builtins.open", mock_open)

    with pytest.raises(ValueError, match="Неожиданная ошибка"):
    
        csv_to_json(str(src_csv), str(dst_csv))


def test_csv_empty_data_with_header(tmp_path):

    """Тест для CSV только с заголовком"""
    
    src = tmp_path / "only_header.csv"
    
    dst = tmp_path / "test.json"

    src.write_text("name,age", encoding="utf-8")
    
    csv_to_json(str(src), str(dst))

    assert dst.exists()
    
    with dst.open(encoding="utf-8") as f:
    
        data = json.load(f)

    assert len(data) == 0  

def test_json_to_csv_wrong_extension(tmp_path):

    """Тест: JSON файл с неправильным расширением"""
    
    src = tmp_path / "test.txt"  # Не .json файл
    
    dst = tmp_path / "test.csv"

    src.write_text('[{"name": "test"}]', encoding="utf-8") #json_в_txt_файле

    with pytest.raises(ValueError, match="не является JSON файлом"):
    
        json_to_csv(str(src), str(dst))


def test_csv_to_json_wrong_extension(tmp_path):

    """Тест: CSV файл с неправильным расширением"""
    
    src = tmp_path / "test.txt"  # Не .csv файл
    
    dst = tmp_path / "test.json"

    src.write_text("name,age\nAlice,25", encoding="utf-8")

    with pytest.raises(ValueError, match="не является CSV файлом"):
    
        csv_to_json(str(src), str(dst))
        
 ### Black

![Image alt](https://github.com/JustMause/python_labs/raw/main/images/lab7/01_7.jpg)
 
## Лабораторная работа 8

### Задание 1 (models.py)

from dataclasses import dataclass

from datetime import datetime, date

import re

@dataclass

class Student:

    fio: str
    
    birthdate: str
    
    group: str
    
    gpa: float
    
    def __post_init__(self):
    
        if not re.match(r'^\d{4}-\d{2}-\d{2}$', self.birthdate):
        
            raise ValueError(f"Неверный формат даты: {self.birthdate}. Используйте формат YYYY-MM-DD")
            
        try:
        
            datetime.strptime(self.birthdate, "%Y-%m-%d")
            
        except ValueError:
        
            raise ValueError(f"Неверная дата: {self.birthdate}")
            
        if not (0 <= self.gpa <= 5):

        
            raise ValueError(f"Средний балл должен быть в диапазоне от 0 до 5, получено: {self.gpa}")
        if len(self.fio.split()) < 2:
        
            raise ValueError(f"ФИО должно содержать имя и фамилию: {self.fio}")
    
    def age(self) -> int:
    
        birth_date = datetime.strptime(self.birthdate, "%Y-%m-%d").date()
        
        today = date.today()
        
        age = today.year - birth_date.year
        
        if (today.month, today.day) < (birth_date.month, birth_date.day):
        
            age -= 1
            
        return age
    
    def to_dict(self) -> dict:
    
        return {
        
            "fio": self.fio,
            
            "birthdate": self.birthdate,
            
            "group": self.group,
            
            "gpa": self.gpa
            
        }
    
    @classmethod
    
    def from_dict(cls, data: dict):
    
        return cls(
        
            fio=data.get("fio", ""),
            
            birthdate=data.get("birthdate", ""),
            
            group=data.get("group", ""),
            
            gpa=data.get("gpa", 0.0)
        )
    
    def __str__(self) -> str:
    
        return f"{self.fio}, группа: {self.group}, возраст: {self.age()}, средний балл: {self.gpa}"


if __name__ == "__main__":

    try:
    
        student = Student(
        
            fio="Иванов Иван Иванович",
            
            birthdate="2007-02-19",
            
            group="БИВТ-1-1",
            
            gpa=3.5
        )
        print(student)

        print(f"Словарь: {student.to_dict()}")
        
    except ValueError as e:
    
        print(f"Ошибка: {e}")

![Image alt](https://github.com/JustMause/python_labs/raw/main/images/lab8/01_8.png)

### Задание 2 (serialize.py)

import json

from typing import List

from models import Student

def students_to_json(students: List[Student], path: str) -> None:

    data = [student.to_dict() for student in students]
    
    with open(path, 'w', encoding='utf-8') as f:
    
        json.dump(data, f, ensure_ascii=False, indent=2)
        
    print(f"Данные сохранены в {path}")
    
def students_from_json(path: str) -> List[Student]:

    try:
    
        with open(path, 'r', encoding='utf-8') as f:
        
            data = json.load(f)
            
        students = []
        
        for item in data:
        
            try:
            
                student = Student.from_dict(item)
                
                students.append(student)
                
            except ValueError as e:
            
                print(f"Не удалось создать студента из записи {item}: {e}")
                
        print(f"Загружено {len(students)} студентов из {path}")
        
        return students
        
    except FileNotFoundError:
    
        print(f"Файл {path} не найден")
        
        return []
        
    except json.JSONDecodeError as e:
    
        print(f"Ошибка при чтении JSON файла: {e}")
        
        return []
        
if __name__ == "__main__": 

    students = [
        Student("Иванов Иван Иванович", "2007-02-19", "БИВТ-1-1", 3.5),
        
        Student("Петров Петр Петрович", "2006-01-01", "БИ-2-1", 4.5),
        
        Student("Семёнов Семён Семёнович", "2005-03-03", "ПМ-3-1", 3.9)
    ]
    students_to_json(students, "data/students_output.json")
    
    loaded_students = students_from_json("data/students_input.json")
    
    for student in loaded_students:
    
        print(student)
        
![Image alt](https://github.com/JustMause/python_labs/raw/main/images/lab8/02_8.png)

![Image alt](https://github.com/JustMause/python_labs/raw/main/images/lab8/03_8.png)

## Лабораторная работа 9

### Задание 1 (group.py)

import csv

from pathlib import Path

from models import Student

import sys

from typing import List

sys.path.append(r"C:\Users\Home\lab_python\lab_python-2\src")

class Group():

    def __init__(self, storage_path: str):
    
        self.path = Path(storage_path)
        
        if not self.path.exists():
        
            self.path.write_text("", encoding='utf-8')
            
        if not self.path.read_text(encoding='utf-8').split('\n')[0] == 'fio,birthdate,group,gpa':
        
            raise ValueError('Не корректный заголовок')
            
        with open(self.path, 'r', encoding='utf-8') as f:
        
            rd = list(csv.DictReader(f))
            
            [Student.from_dict(st) for st in rd]

    def _ensure_storage_exists(self):
    
        if not self.path.exists():
        
            self.path.parent.mkdir(parents=True, exist_ok=True)
            
            with open(self.path, 'w', encoding='utf-8') as f:
            
                f.write('fio,birthdate,group,gpa\n')

    def _read_all(self) -> List[dict]:
    
        self._ensure_storage_exists()
        
        with open(self.path, 'r', encoding='utf-8') as f:
        
            return list(csv.DictReader(f))

    def list(self):
    
        with open(self.path, 'r', encoding='utf-8') as f:
        
            rd = csv.reader(f)
            
            next(rd)
            
            Students = list(rd)
            
        return Students
    
    def _write_all(self, Students: List[dict]):
    
        with open(self.path, 'w', encoding='utf-8', newline='') as f:
        
            writer = csv.DictWriter(f, fieldnames=['fio', 'birthdate', 'group', 'gpa'])
            
            writer.writeheader()
            
            writer.writerows(Students)

    def add(self, Student: Student):
    
        rows = self._read_all()
        
        if any(row['fio'] == Student.fio for row in rows):
        
            raise ValueError(f"Студент {Student.fio} уже существует")
            
        rows.append({
        
            'fio': Student.fio,
            
            'birthdate': Student.birthdate,
            
            'group': Student.group,
            
            'gpa': str(Student.gpa)
        })
        self._write_all(rows)
    

    def find(self, substr: str):
    
        with open(self.path, 'r', encoding='utf-8') as f:
        
            rd = list(csv.DictReader(f))
            
        return [Student.from_dict(r) for r in rd if substr in r['fio']]
    
    def remove(self, fio: str):
    
        with open(self.path, 'r', encoding='utf-8') as f:
        
            rd = csv.DictReader(f)
            
            data_new = [r for r in rd if fio not in r['fio']]
            
        with open(self.path, 'w', newline='', encoding='utf-8') as f:
        
            wr = csv.DictWriter(f, fieldnames=list(data_new[0].keys()))
            
            wr.writeheader()
            
            wr.writerows(data_new)

    def update(self, fio: str, **fields):
    
        data = Student.from_dict({'fio': fio, **fields}).to_dict()
        
        data.pop('fio')
        
        with open(self.path, 'r', encoding='utf-8') as f:
        
            rd = list(csv.DictReader(f))
            
            for r in rd:
            
                if fio in r['fio']:
                
                    r.update(data)
                    
                    break 
                    
        with open(self.path, 'w', newline='', encoding='utf-8') as f:
        
            wr = csv.DictWriter(f, fieldnames=list(rd[0].keys()))
            
            wr.writeheader()
            
            wr.writerows(rd)
    
if __name__ == "__main__":

     group = Group(r'C:\Users\Home\lab_python\lab_python-2\data\students.csv')

### list() — вернуть всех студентов в виде списка Student

![Image alt](https://github.com/JustMause/python_labs/raw/main/images/lab9/01_9.jpg)

### add(student) — добавить нового студента в CSV

![Image alt](https://github.com/JustMause/python_labs/raw/main/images/lab9/02_9.png)

### find(substr) — найти студентов по подстроке в fiofind(substr) — найти студентов по подстроке в fio

![Image alt](https://github.com/JustMause/python_labs/raw/main/images/lab9/03_9.jpg)

### remove(fio) — удалить запись(и) с данным fio

![Image alt](https://github.com/JustMause/python_labs/raw/main/images/lab9/04_9.jpg)

### update(fio, **fields) — обновить поля существующего студента

![Image alt](https://github.com/JustMause/python_labs/raw/main/images/lab9/02_9.png)

## Лабораторная работа 10

### Задание 1 (structures.py)

from collections import deque

from typing import Any, Optional


class Stack:
    
    __slots__ = ("_data",)

    def __init__(self, iterable=None) -> None:
    
        self._data: list[Any] = list(iterable) if iterable is not None else []

    def push(self, item: Any) -> None: 
    
        self._data.append(item)

    def pop(self) -> Any:
    
        if not self._data:
        
            raise IndexError("pop from empty Stack")
            
        return self._data.pop()

  # Метод просмотра верхнего элемента без удаления
  
    def peek(self) -> Optional[Any]:
    
        return self._data[-1] if self._data else None

    # Метод проверки стека на пустоту
    
    def is_empty(self) -> bool:
    
        return not self._data

    def __len__(self) -> int:
    
        return len(self._data)

    def __repr__(self) -> str:
    
        return f"Stack({self._data!r})"


class Queue:

    __slots__ = ("_data",)

    def __init__(self, iterable=None) -> None:
    
        self._data: deque[Any] = deque(iterable) if iterable is not None else deque()

    def enqueue(self, item: Any) -> None:
    
        self._data.append(item)

    def dequeue(self) -> Any:
    
        if not self._data:
        
            raise IndexError("dequeue from empty Queue")
            
        return self._data.popleft()

    def peek(self) -> Optional[Any]:
    
        return self._data[0] if self._data else None

    def is_empty(self) -> bool:
    
        return not self._data

    def __len__(self) -> int:
    
        return len(self._data)

    def __repr__(self) -> str:
    
        return f"Queue({list(self._data)!r})"

print('Stack')

stack = Stack([1,2,3,4])

print(f'Снятие верхнего элемента стека : {stack.pop()}')

print(f'Пустой ли стек? {stack.is_empty()}')

print(f'Число сверху : {stack.peek()}')

stack.push(1)

print(f'Значение сверху после добавления числа в стек : {stack.peek()}')

print(f'Длина стека : {len(stack)}')

print(f'Стек : {stack._data}')

print('Deque')

q = Queue([1,2,3,4])

print(f'Значение первого эллемента : {q.peek()}')

q.dequeue()

print(f'Значение первого эллемента после удаления числа : {q.peek()}')

q.enqueue(41)

print(f'Значение первого эллемента после добавления числа : {q.peek()}')

print(f'Пустая ли очередь? {q.is_empty()}')

print(f'Количество элементов в очереди : {len(q)}')

![Image alt](https://github.com/JustMause/python_labs/raw/main/images/lab10/01_10.jpg)

### Задание 2 (linked_list.py)

from typing import Any, Iterator, Optional


class Node:

    __slots__ = ("value", "next")

    def __init__(self, value: Any, next: Optional["Node"] = None) -> None:
    
        self.value = value
        
        self.next = next

    def __repr__(self) -> str:
    
        return f"Node({self.value!r})"


class SinglyLinkedList:

    __slots__ = ("head", "tail", "_size")

    def __init__(self, iterable=None) -> None:
    
        self.head: Optional[Node] = None
        
        self.tail: Optional[Node] = None
        
        self._size: int = 0
        
        if iterable:
        
            for v in iterable:
            
                self.append(v)

    def append(self, value: Any) -> None:
    
        """Добавить в конец — O(1)."""
        
        node = Node(value)
        
        if not self.head:
        
            self.head = node
            
            self.tail = node
            
        else:
            assert self.tail is not None
            
            self.tail.next = node
            
            self.tail = node
            
        self._size += 1

    def prepend(self, value: Any) -> None:
    
        """Добавить в начало — O(1)."""
        
        node = Node(value, next=self.head)
        
        self.head = node
        
        if self._size == 0:
        
            self.tail = node
            
        self._size += 1

    def insert(self, idx: int, value: Any) -> None:
    
        """Вставить по индексу. Допускаются idx==0 и idx==len."""
        
        if idx < 0 or idx > self._size:
        
            raise IndexError("insert index out of range")
            
        if idx == 0:
        
            self.prepend(value)
            
            return
            
        if idx == self._size:
        
            self.append(value)
            
            return

        prev = self.head
        
        for _ in range(idx - 1):
        
            assert prev is not None
            
            prev = prev.next
            
        assert prev is not None
        
        node = Node(value, next=prev.next)
        
        prev.next = node
        
        self._size += 1

    def remove(self, value: Any) -> None:
    
        """Удалить первое вхождение value. Если не найдено — ValueError."""
        
        prev: Optional[Node] = None
        
        cur = self.head
        
        idx = 0
        
        while cur:
        
            if cur.value == value:
            
                if prev is None:
                
                    self.head = cur.next
                    
                else:
                    prev.next = cur.next
                    
                if cur is self.tail:
                
                    self.tail = prev
                    
                self._size -= 1
                
                return
            prev, cur = cur, cur.next
            
            idx += 1
            
        raise ValueError("remove: value not found in SinglyLinkedList")

    def remove_at(self, idx: int) -> None:
    
        """Удалить элемент по индексу. Возбуждает IndexError при неверном индексе."""
        
        if idx < 0 or idx >= self._size:
        
            raise IndexError("remove_at index out of range")
            
        prev: Optional[Node] = None
        
        cur = self.head
        
        for _ in range(idx):
        
            prev, cur = cur, cur.next  # type: ignore
            
        assert cur is not None
        
        if prev is None:
        
            self.head = cur.next
            
        else:
        
            prev.next = cur.next
            
        if cur is self.tail:
        
            self.tail = prev
            
        self._size -= 1

    def __iter__(self) -> Iterator[Any]:
    
        cur = self.head
        
        while cur:
        
            yield cur.value
            
            cur = cur.next

    def __len__(self) -> int:
    
        return self._size

    def __repr__(self) -> str:
    
        return f"SinglyLinkedList([{', '.join(repr(x) for x in self)}])"

    def __str__(self) -> str:
    
        parts = []
        
        cur = self.head
        
        while cur:
        
            parts.append(f"[{cur.value!s}]")
            
            cur = cur.next
            
        parts.append("None")
        
        return " -> ".join(parts)

sll = SinglyLinkedList()

print(f'Длина нашего односвязанного списка : {len(sll)}')

sll.append(1)

sll.append(2)

sll.prepend(0)

print(f'Наша ныняшняя длина списка после добавления эллементов : {len(sll)}') 

print(f'Односвязаный список : {list(sll)}')

sll.insert(1, 0.5)

print(f'Длина списка после добавления на 1 индекс числа 0.5 : {len(sll)}')

print(f'Односвязаный список : {list(sll)}')

sll.append(41)

print(f'Односвязанный список после добавления числа в конец : {list(sll)}')

print(sll) 

![Image alt](https://github.com/JustMause/python_labs/raw/main/images/lab10/02_10.jpg)

## Теория

### Стек (Stack)

Принцип: LIFO — Last In, First Out. Операции: push(x) — положить элемент сверху; pop() — снять верхний элемент; peek() — посмотреть верхний, не снимая. Типичные применения: история действий (undo/redo); обход графа/дерева в глубину (DFS); парсинг выражений, проверка скобок.

Асимптотика (при реализации на массиве / списке): push — O(1) амортизированно; pop — O(1); peek — O(1); проверка пустоты — O(1). Очередь (Queue) Принцип: FIFO — First In, First Out.

Операции: enqueue(x) — добавить в конец; dequeue() — взять элемент из начала; peek() — посмотреть первый элемент, не удаляя.

Типичные применения: обработка задач по очереди (job queue); обход графа/дерева в ширину (BFS); буферы (сетевые, файловые, очереди сообщений).

В Python: обычный list плохо подходит для реализации очереди: удаление с начала pop(0) — это O(n) (все элементы сдвигаются); collections.deque даёт O(1) операции по краям: append / appendleft — O(1); pop / popleft — O(1).

Асимптотика (на нормальной очереди): enqueue — O(1); dequeue — O(1); peek — O(1). Односвязный список (Singly Linked List)

Структура: состоит из узлов Node; каждый узел хранит: value — значение элемента; next — ссылку на следующий узел или None (если это последний).

Основные идеи: элементы не хранятся подряд в памяти, как в массиве; каждый элемент знает только «следующего соседа».

Плюсы: вставка/удаление в начало списка за O(1): если есть ссылка на голову (head), достаточно перенаправить одну ссылку; при удалении из середины не нужно сдвигать остальные элементы: достаточно обновить ссылки узлов; удобно использовать как базовый строительный блок для других структур (например, для очередей, стеков, хеш-таблиц с цепочками). Минусы:

доступ по индексу i — O(n): чтобы добраться до позиции i, нужно пройти i шагов от головы; нет быстрого доступа к предыдущему элементу: чтобы удалить узел, нужно знать его предыдущий узел → часто нужен дополнительный проход. Типичные оценки:

prepend (добавить в начало) — O(1); append: при наличии tail — O(1), без tail — O(n), т.к. требуется пройти до конца; поиск по значению — O(n). Двусвязный список (Doubly Linked List) Структура:

также состоит из узлов DNode; каждый узел хранит: value — значение элемента; next — ссылку на следующий узел; prev — ссылку на предыдущий узел. Основные идеи:

можно двигаться как вперёд, так и назад по цепочке узлов; удобно хранить ссылки на оба конца: head и tail. Плюсы по сравнению с односвязным:

удаление узла по ссылке на него — O(1): достаточно «вытащить» его, перенастроив prev.next и next.prev; не нужно искать предыдущий узел линейным проходом; эффективен для структур, где часто нужно удалять/добавлять элементы в середине, имея на них прямые ссылки (например, реализация LRU-кэша); можно легко идти в обе стороны: прямой и обратный обход списка.

Минусы: узел занимает больше памяти: нужно хранить две ссылки (prev, next); код более сложный: легко забыть обновить одну из ссылок и «сломать» структуру; сложнее отлаживать.

Типичные оценки (при наличии head и tail): вставка/удаление в начале/конце — O(1); вставка/удаление по ссылке на узел — O(1); доступ по индексу — O(n) (нужно идти от головы или хвоста); поиск по значению — O(n).

Пример текстовой визуализации: None <- [A] <-> [B] <-> [C] -> None
