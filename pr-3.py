c1 = int(input('Введите целое число: '))
c2 = int(input('Введите целое число: '))
c3 = int(input('Введите целое число: '))

lst = []

if 1 <= c1 <= 3:
    lst.append(c1)
if 1 <= c2 <= 3:
    lst.append(c2)
if 1 <= c3 <= 3:
    lst.append(c3)

print('Интервалу принадлежат: ', lst)


c1 = input('Введите целое число: ')
c2 = input('Введите целое число: ')

if c1 > c2:
    print(c1)
elif c1 == c2:
    print('Числа равны')
else:
    print('Наибольшее число: ', c2)


c = int(input('Введите целое число: '))

if c % 2 == 0:
    print('Число чётное')
else:
    print('Число нечётное')


c = str(input('Введите целое число: '))

chet = []
nechet = []

for n in range(0, len(c)):
    if int(c[n]) % 2 == 0:
        chet.append(c[n])
    else:
        nechet.append(c[n])

print('Чётные цифры: ', chet)
print('Нечётные цифры: ', nechet)


c = int(input('Введите целое число: '))
delit = []

for d in range(2, c // 2 + 1):
    if c % d == 0:
        delit.append(d)

if len(delit) == 0:
    print('Число ', c, ' - простое')
else:
    print('Число ', c, 'не является простым')


c1 = int(input('Введите целое число: '))
c2 = int(input('Введите целое число: '))
c3 = int(input('Введите целое число: '))

sa = (c1 + c2 + c3) / 3

print('Среднее арифм. трёх чисел равно ', sa)


c = int(input('Введите целое число: '))

if c % 7 == 0:
    print('Число кратно семи')
else:
    print('Число не кратно семи')


c = int(input('Введите год: '))

if c % 4 == 0:
    print('Год високосный')
else:
    print('год не високосный')


c = int(input('Введите номер месяца: '))

if c == 2:
    y = input('Какой сейчас год? ')
    if y % 4 == 0:
        print('В этом месяце 29 дней')
    else:
        print('В этом месяце 28 дней')
elif c == 4 or c == 6 or c == 9 or c == 11:
    print('В этом месяце 30 дней')
elif c == 1 or c == 3 or c == 5 or c == 7 or c == 8 or c == 10 or c == 12:
    print('В этом месяце 31 день')
else:
    print('Такоогго месяца нет')


a = int(input('Введите сторону треугольника: '))
b = int(input('Введите сторону треугольника: '))
c = int(input('Введите сторону треугольника: '))
p = (a + b + c) / 2
S = (p * (p - a) + (p - b) * (p - c)) ** 0.5
print('Площадь треугольника равна ', S)


a = int(input('Введите целое число: '))
b = int(input('Введите целое число: '))
c = int(input('Введите целое число: '))

if a == b and b == c:
    print('Все числа равны')
elif a != b and b != c and a != c:
    print('Числа неравны')
else:
    print('Два числа равны')


age = input('Введите ваш возраст: ')
print('Ваш возраст ', age, 'лет')


c = int(input('Введите целое число: '))

if c > 0:
    print('Число положительное')
elif c < 0:
    print('Число отрицательное')
else:
    print('Это число "ноль"')


y = int(input('Какой сейчас год? '))
if y % 4 == 0:
    print('В этом году в феврале 29 дней')
else:
    print('В этом году в феврале 28 дней')


x = int(input('Введите координаты точки  по x: '))
y = int(input('Введите координаты точки  по y: '))

if 0 <= x <= 5 and 0 <= y <= 5:
    print('Точка принадлежит квадрату')
else:
    print('Точка не принадлежит квадрату')


a = int(input('Введите целое число: '))
b = int(input('Введите целое число: '))

print('сумма = ', a + b)
print('разность = ', abs(a) - abs(b))


c = int(input('Введите целое число: '))
if c % 3 == 0 and c % 5 == 0:
    print('Число кратно 3 и 5')
elif c % 3 == 0 and c % 5 != 0:
    print('Число кратно 3-м')
elif c % 3 != 0 and c % 5 == 0:
    print('Число кратно 5-и')
else:
    print('Число не кратно ни 3-м, ни 5-и')


c = int(input('Введите год: '))

if c % 100 == 0:
    print('Год вековой')
else:
    print('год не вековой')


c = str(input('Введите число: '))

if c.count('.') == 1 or c.count(',') == 1:
    print('Число дробное')
else:
    print('Число целое')
