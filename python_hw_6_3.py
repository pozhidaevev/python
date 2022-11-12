class Worker():
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):
    def get_full_name(self):
        print(f'Имя и фамилия сотрудника: {self.name} {self.surname}')

    def get_total_income(self):
        res = self._income.get('wage') + self._income.get('bonus')
        print(f'Доход с учетом премии: {res}')


person = Position('John', 'Malkovich', 'actor', 5000, 153000)
print(person.name)
print(person.surname)
print(person.position)
print(person._income)
person.get_full_name()
person.get_total_income()
print('***********************')

person = Position('Bruce', 'Willis', 'actor', 25000, 55000)
print(person.name)
print(person.surname)
print(person.position)
print(person._income)
person.get_full_name()
person.get_total_income()