from collections import Counter
from pyy import fy


def ff(x):
    print("Элемент | Частота")
    return Counter(x)
     
x = fy(n)
v = ff(x)
print(*[f'{i} | {v[i]}' for i in v] , sep = '\n')
