s = 'Задания для самостоятельной работы (по вариантам)'


#  6
s = s.lower()
k = s.count('а')
s.replace('a', '')
print('Кол-во замен: ', k)


#  13
c1 = s.find('(')
c2 = s.find(')')
print(s[c1 + 1 : c2])


#  5
s = s.lower()
print(s)
