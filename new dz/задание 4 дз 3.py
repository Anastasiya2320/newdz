def f(x):
    while x:
        list.append(x)
        x = input("Ввод: ")
    lst = []
    print("Элемент | Частота")
    c = Counter(a)
    return c
    #for t in list:
        #if t not in lst:
        #    print(t, "|", list.count(t))
        #   lst.append(t)


x = input("Ввод: ")
v = f(x)
print(*[f'{i} | {v[i]}' for i in v] , sep = '\n')
