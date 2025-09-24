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
