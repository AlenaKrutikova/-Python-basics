import math

print('Введите выражение')
str = input()
result = 0

if str.find('+') != -1:
    lst = str.split('+')
    result = int(lst[0]) + int(lst[1])

elif str.find('*') != -1:
    lst = str.split('*')
    result = int(lst[0]) * int(lst[1])

elif str.find('/') != -1:
    lst = str.split('/')
    result = int(lst[0]) / int(lst[1])

elif str.find('^') != -1:
    lst = str.split('^')
    result = int(lst[0]) ** int(lst[1])

elif str.find('!') != -1:
    lst = str.split('!')
    if int(lst[0]) < 0 : result = 'Выражение некорректно'
    else: result = math.factorial(int(lst[0]))

elif str.find('-') != -1:
    lst = str.split('-')
    i = 0
    while (1):
        if lst[i] == '':
            lst.remove(lst[i])
            lst[i] = '-' + lst[i]
        if i < len(lst) - 1: i += 1
        else: break
    result = int(lst[0]) - int(lst[1])

else: print('Выражение некорректно')    
print(result)
