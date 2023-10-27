#  в9
#  1

n = int(65)


def d(a):
    m = 0
    for i in range(len(str(a))):
        m = int(str(a)[i]) + m
    a = a - m
    return a


k = 0
while n != 0:
    n = d(n)
    k += 1
print(k)


#  2

lst1, lst2, lst3 = [1, 2, 3], [4, 5, 6], [7, 8, 9]


def f(a):
    c = 1
    for i in range(len(a)):
        c = c * int(str(a[i]))
    return c


def f1(a):
    c = 0
    for i in range(len(a)):
        c = c + int(str(a[i]))
    return c / len(a)


print(f(lst1), f(lst2), f(lst3))
print(f1(lst1), f1(lst2), f1(lst3))


#  в10
# 1

a, b, c = '4', '2', '1'
k = 0

for i in range(100, 222 + 1):
    if str(i).find(a) >= 0 and str(i).find(b) >= 0 and str(i).find(c) >= 0:
        k += 1

print(k)


#  2

s = 'очень хочется есть'
s = s.split(' ')
s1 = ''
for i in range(len(s) - 1, 0 - 1, -1):
    s1 += str(s[i]) + ' '

print(s1)