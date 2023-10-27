#  14
#  1
lst = [int(input('введите число: ')) for i in range(10 + 1)]
print(lst)

max = 0
min = float('inf')
for i in lst:
    if max < i:
        max = i
    if min > i:
        min = i
lst[lst.index(min)], lst[lst.index(max)] = lst[lst.index(max)], lst[lst.index(min)]
print(lst)


#  2
lst = [int(input('введите число: ')) for i in range(10 + 1)]
print(lst)

sa = sum(lst) / len(lst)
for i in range(len(lst) + 1):
    if lst[i] > sa:
        lst[i] = 1

print(lst)


#  10
#  1

lst = [int(i) for i in range(25 + 1)]
lst1 = []

for i in range(len(lst)):
    if lst.count(lst[i]) >1:
        lst1.append(lst[i])

if len(lst1) == 0:
    print('одинаковых значений нет')
else:
    print(lst1)


#  2

lst = [int(i) for i in range(15 + 1)]
lst1 = []

for i in range(len(lst)):
    if lst[i] < 10:
        lst1.append(int(0))
    elif lst[i] > 20:
        lst1.append(int(1))
    else:
        lst1.append(lst[i])

print(lst, lst1)