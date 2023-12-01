file = open('БачуринаДН_УБ-32_vvod.txt', encoding="utf-8").readlines()
A = []

for i in file:
    c = i.replace('\n', '')
    lst = []
    for j in c.split():
        lst.append(int(j))
    A.append(lst)

for i in range(len(A)):
    for j in range(len(A[i])):
        if A[i][j] > 0:
            A[i][j] = 1
        elif A[i][j] < 0:
            A[i][j] = 0

s = ''
for i in A:
    k = 0
    for j in i:
        s += str(j) + ' '
        k += 1
        if k == len(i):
            s += '\n'

file = open('БачуринаДН_УБ-32_vivod.txt', 'w')
file.write(s)
file.close()



