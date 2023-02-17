
list = [1,2,3,4,5,8,15,23,38]
list2 = []

for i in list:
    if i%2 == 0:
        list2.append((i,i ** 3))


print(list2)