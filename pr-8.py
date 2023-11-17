#  V4
#  №1

A = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
summ = []
for i in range(len(A)):
    summ.append(sum(A[i]))
print(A[summ.index(max(summ))], max(summ))
print(A[summ.index(min(summ))], min(summ))


#  №2

A = [[-5, -4, -2], [-1, 0, 1], [2, 3, 4]]
for i in range(len(A)):
    for j in range(len(A[i])):
        if A[i][j] > 0:
            A[i][j] = 1
        elif A[i][j] < 0:
            A[i][j] = 0

for i in range(len(A)):
    for j in range(len(A[i])):
        print(A[i][j], end='')
    print()


# V5
#  1

A = [[-9, 6, -20, 0], [1, 3, 40], [2, 4, 9]]
for i in range(len(A)):
    A[i] = sorted(A[i])
print(A)

#  2

A = [[-9, 6, -20, 0], [1, 3, 40], [2, 4, 9]]
for i in range(len(A)):
    A[i][A[i].index(min(A[i]))] = A[i][A[i].index(min(A[i]))] % 2


for i in range(len(A)):
    for j in range(len(A[i])):
        print(A[i][j], end='')
    print()
