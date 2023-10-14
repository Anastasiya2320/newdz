from collections import Counter

text = input().split()

def f(text):
    u = max(text, key = len)
    c = Counter(text).most_common(1)[0][0]
    a = max(c, key = lambda x: c[x])
    print('самое длиное:' + u + "самое частое:" + c )
f(text)
