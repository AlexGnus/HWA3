'''Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N]. 
Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
 В последующих строках записаны N целых чисел Ai. Последняя строка содержит число X.
Пример:

5
1 2 3 4 5
3
-> 1'''

from random import randint
b = int(input('Введите количество элементов в массиве: '))
lst = []
for i in range(b):
    lst.append(randint(0,10))
print(lst)
x = int(input('Введите число х: '))
a = lst.count(x) # можно было посчитать количество элементов циклом, увеличивая счетчик5
print(a)