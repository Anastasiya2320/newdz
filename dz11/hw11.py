class Time:
    def __init__(self, h = 0, m = 0, s = 0):
        self.h = h
        self.m = m
        self.s = s

    def input_time(self):
        while True:
            self.h = int(input("введите часы: "))
            self.m = int(input("введите минуты: "))
            self.s = int(input("введите секунды: "))
             if self.h > 23 or self.m > 59 or self.s > 59 or self.h < 0 or self.m < 0 or self.s < 0:
               print('ошибка')
            else:
               break

    def __str__(self):
       return f"время: {self.h:02d}:{self.m:02d}:{self.s:02d}" 
'''    
t = Time()
t.input_time()
print(t)       
'''
