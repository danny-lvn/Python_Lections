#value = None
#a = 123  # int
#b = 1.23 # float

#s = 'hello world'
#print(s)
#print (a, b, s)
#print (a, '-', b, '-', s)
#print ('{} - {} - {}'.format(a, b, s))
#print ('{1} - {2} - {0}'.format(a, b, s)) # изменения порядка вывода
#print (f'{a} - {b} - {s}')

#f = True
#print(f)

#list = ['1', '2', '3']
#col = ['hello', 1, 3.42, True]
#print(list)
#print(col)

#print('Введите a')
#a = float(input())
#print('Введите b')
#b = float(input())
#print(a, '+', b, '=', a + b)
#print (f'{a} {b}')

#f = [1, 2, 3, 4]
#print(f)
#print(not 2 in f)

#is_odd = not f[0] % 2
#print(is_odd)

"""
a = int(input('a = '))
b = int(input('b = '))
if a > b:
    print(a)
else:
    print(b)
"""
'''
username = input('Введите имя: ')
if username == 'Маша':
    print('Ура, это же МАША!')
elif username == 'Марина':
    print('Я так ждала Вас, Марина!')
elif username == 'Ильнар':
    print('Ильнар - топ)')
else:
    print('Привет, ', username)
'''
'''
original = 23
inverted = 0
while original != 0:
     inverted = inverted * 10 + (original % 10)
     original //= 10
else:
    print('Пожалуй')
    print('хватит')
print(inverted)
'''
'''
for i in range(1, 10, 2):
    print(i)

for i in 'qwerty':
    print(i)
'''
'''
text = 'съешь ещё этих мягких французских булок'
print(len(text))
print('ещё' in text)
print(text.isdigit())
print(text.islower())
print(text.replace('ещё','ЕЩЁ'))
'''
'''
text = 'съешь ещё этих мягких французских булок'
print(text[0])
print(text[len(text)-1])
print(text[-5])
print(text[0:5])
'''
'''
numbers = [1, 2, 3, 4, 5]
print(numbers)  # [1, 2, 3, 4, 5]
numbers = list(range(1, 6))
print(numbers)  # [1, 2, 3, 4, 5]
numbers[0] = 10
print(numbers)  # [10, 2, 3, 4, 5]
for i in numbers:
    i *= 2
    print(i)    # [20, 4, 6, 8, 10]
print(numbers)  # [10, 2, 3, 4, 5]
'''
'''
colors = ['red', 'green', 'blue']
#for e in colors:
#    print(e)
colors.append('gray')
print(colors == ['red', 'green', 'blue', 'gray'])
colors.remove('red')
del colors[0]
for e in colors:
    print(e)
'''

def f(x):
    if x == 1:
        return 'Целое'
    elif x == 2.3:
        return 23
    else:
        return

arg = 2
print(f(arg))
print(type(f(arg)))