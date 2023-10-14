def season(n):
    if n in [1, 2, 12]:
        return "Зима"
    if n in [3, 4, 5]:
        return "Весна"
    if n in [6, 7, 8]:
        return "Лето"
    return "Осень"


n = int(input("Месяц: "))
season(n)
