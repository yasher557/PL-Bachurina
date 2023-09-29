#  1

a, b = int(input('введите число: ')), int(input('введите число: '))
for i in range(a, b + 1):
    print(i)


#  2

a, b = int(input('введите число: ')), int(input('введите число: '))
if a < b:
    for i in range(a, b + 1):
        print(i)
else:
    for i in range(a, b + 1, -1):
        print(i)


#  3

a, b = int(input('введите число: ')), int(input('введите число: '))
for i in range(a, b + 1, -1):
    if i % 2 != 0:
        print(i)


#  4

n = int(input('введите количество: '))
summ = 0
for i in range(n + 1):
    summ += int(input('введите число: '))
print(summ)


#  5

n = int(input('введите число: '))
summ = 0
for i in range(n + 1):
    summ += n ** 3
print(summ)


#  6

n = int(input('введите число: '))
fact = 1
for i in range(1, n + 1):
    fact = fact * i
print(fact)


#  7

n = int(input('введите число: '))
summ = 0
fact = 1
for i in range(1, n + 1):
    fact = fact * i
    summ += fact
print(summ)


#  8

n = int(input('введите число: '))
st = 0
for i in range(1, n + 1):
    for c in range(1, i + 1):
        st += c
    print(st)


#  9

lst = [0, 1]
n = int(input('введите число: '))
for i in range(1, n + 1):
    lst.append(lst[-2] + lst[-1])
print(sum(lst))


#  10

lst = [0, 1]
n, k = int(input('введите число: ')), int(input('введите число: ')) - 1
for i in range(1, n + 1):
    lst.append(lst[-2] + lst[-1])
print(sum(lst[k: len(lst)]))
