a = input()
b = []
while a:
    b.append(a)
    a = input()
b.sort(reverse=True) # сортировка элементов числового списка по убыванию
print(''.join(b))  #join в качестве аргумента b он получает список, элементы которого и будет объединять в строку, a '' — это разделитель. Hужно указать пустую строку, eсли мы не хотим его устанавливать   
 
