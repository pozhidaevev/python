class Date:
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

    @classmethod
    def change_type(cls, data):
        d = int(my_date.split('-')[0])
        m = int(my_date.split('-')[1])
        y = int(my_date.split('-')[2])
        data = [d, m, y]
        return cls(d, m, y)

    @staticmethod
    def valid_number(obj):
        if obj.day not in range(1,32):
            return f'Число должно быть в диапазоне 1-31. Исправьте!'
        if obj.month not in range(1,13):
            return f'Месяц должен быть в диапазоне 1-12. Исправьте!'
        if obj.year not in range(1991,2023):
            return f'Год должен быть в диапазоне 1991-2022. Исправьте!'

my_date = '15-22-2011'

a = Date.change_type(my_date)
print(a.day, a.month, a.year)
print(Date.valid_number(a))