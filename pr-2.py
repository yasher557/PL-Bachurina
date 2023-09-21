import math

#  №6

x = 16.55 * 10 ** (-3)
y = -2.75
z = 0.15

s = (10 * (x ** (1 / 3) + x ** (y + 2))) ** 0.5 * ((math.asin(z)) ** 2 - abs(x - y))

print('{0:.4f}'.format(s))

#  №11

x = 6.251
y = 0.827
z = 25.001

s = y ** (abs(x) ** (1 / 3)) + math.cos(y) ** 3 * (abs(x - y) * (1 + (math.sin(z) ** 2 / (x + y) ** 0/5)) / (math.e ** abs(x - y) + x / 2))

print('{0:.4f}'.format(s))

#  №1

x = 14.26
y = -1.22
z = 3.5 * 10 ** (-2)

s = ((2 * math.cos(x - 2 / 3)) / (1 / 2 + (math.sin(y)) ** 2)) * (1 + (z ** 2 / (3 - z ** 2 / 5)))

print('{0:.4f}'.format(s))
