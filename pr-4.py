a, b = int(input('введите число: ')), int(input('введите число: '))
for i in range(a, b + 1):
    print(i)


a, b = int(input('введите число: ')), int(input('введите число: '))
if a < b:
    for i in range(a, b + 1):
        print(i)
else:
    for i in range(a, b + 1, -1):
        print(i)


a, b = int(input('введите число: ')), int(input('введите число: '))
for i in range(a, b + 1, -1):
    if i % 2 != 0:
        print(i)


n = int(input('введите количество: '))
summ = 0
for i in range(n + 1):
    summ += int(input('введите число: '))
print(summ)


n = int(input('введите число: '))
summ = 0
for i in range(n + 1):
    summ += n ** 3
print(summ)


n = int(input('введите число: '))
fact = 1
for i in range(1, n + 1):
    fact = fact * i
print(fact)


n = int(input('введите число: '))
summ = 0
fact = 1
for i in range(1, n + 1):
    fact = fact * i
    summ += fact
print(summ)

n = int(input('введите число: '))
st = 0
for i in range(1, n + 1):
    for c in range(1, i + 1):
        st += c
    print(st)


lst = [0, 1]
n = int(input('введите число: '))
for i in range(1, n + 1):
    lst.append(lst[-2] + lst[-1])
print(sum(lst))


lst = [0, 1]
n, k = int(input('введите число: ')), int(input('введите число: '))
for i in range(1, n + 1):
    lst.append(lst[-2] + lst[-1])
print(sum(lst[k: len(lst)]))
