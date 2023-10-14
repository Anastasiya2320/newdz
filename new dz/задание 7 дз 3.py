from collections import Counter

def f(text):
    u = max(text, key = len)
    c = Counter(text).most_common(1)[0][0]
    a = max(c, key = lambda x: c[x])
    print('самое длиное:' + u + "самое частое:" + c )


text = input().split()
f(text)
