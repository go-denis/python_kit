"""
На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной. Выведите минимальное количество монет, которые нужно перевернуть
*Пример:
5 -> 1 0 1 1 0
2
*
"""
"""
data = [1,2,3,5,8,15,23,38]

res = list()

for i in data:
    if i % 2 == 0:
        res.append((i, i ** 2))
print(res)
"""

def select(f, col):
    return [f(x) for x in col]

def where(f, col):
    return [x for x in col if f(x)]

data = [1,2,3,5,8,15,23,38]
res  = select(int, data)
print(res)
res  = where(lambda x: x % 2 == 0, res)
print(res)

res = select(lambda x: (x, x ** 2), res)
