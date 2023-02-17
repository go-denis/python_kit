data = [1,2,3,4,5,8,15,23,38]
def sselect(f, col):
    return [f(x) for x in col]

def where(f, col):
    return [x for x in col if f(x)]

res = sselect(int, data)
print(res)
res = where(lambda x: x % 2 == 0, res)
print(res)
#res = list(sselect(lambda x: (x,x**2), res)) тоже самое что ниже
res = list(map(lambda x: (x,x**2), res)) 
print(res)