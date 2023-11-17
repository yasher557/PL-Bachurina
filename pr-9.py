#  A
#  1

def ost(a, b):
    if a - b <= 0:
        return a
    return ost(a - b, b)


print(ost(113, 27))


#  B
#  2


def m():
    a = int(input('введите число: '))
    if a == 0:
        return 0
    N = m()
    if a < N:
        print(N)
    else:
        print(a)


print(m())
