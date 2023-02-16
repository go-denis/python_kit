"""
Даны два неупорядоченных набора целых чисел (может быть, с повторениями). Выдать без повторений в порядке возрастания 
все те числа, которые встречаются в обоих наборах. Пользователь вводит 2 числа. n - кол-во элементов первого множества.
m - кол-во элементов второго множества. Затем пользователь вводит сами элементы множеств.

Пример:
11 6
2 4 6 8 10 12 10 8 6 4 2
3 6 9 12 15 18
6 12
"""
import random



#Генерируем списки
def rendNum(num):
    list = []
    for i in  range(num):
        #newNum = int(input("Введите число: "))
        list.append(int(input("Введите число: ")))
    
    return list

#n = rendNum(int(input("Введите кол-во элементов всторого множества: " )))
#m = rendNum(int(input("Введите кол-во элементов всторого множества: " )))


def chekNum(list1, list2):
    chekList = []
    list3 = list1 + list2

    for i in list3:
        if list3.count(i) > 1 and i not in chekList:
            chekList.append(i)

    return chekList
        



print(chekNum(rendNum(int(input("Введите кол-во элементов всторого множества: " ))),rendNum(int(input("Введите кол-во элементов всторого множества: " )))))