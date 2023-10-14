from collections import Counter
from задание 1 дз 3 import fy


def ff(x):
    print("Элемент | Частота")
    return Counter(x)
     
x = fy(n)
v = ff(x)
print(*[f'{i} | {v[i]}' for i in v] , sep = '\n')
