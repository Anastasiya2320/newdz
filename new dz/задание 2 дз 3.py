def Season(n):
    if n in [1, 2, 12]:
        return ("Зима")
    elif n in [3, 4, 5]:
        return ("Весна")
    elif n in [6, 7, 8]:
        return ("Лето")
    else:
        return ("Осень")


n = int(input("Месяц: "))
Season(n)
