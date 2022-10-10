revenue = int(input('Укажите выручку компании (в рублях): '))
costs = int(input('Укажите издержки компании (в рублях): '))
profit = revenue - costs
if profit < 0:
    print(f'Ваша компания работает в убыток. Он составляет: {profit} рублей.')
elif profit == 0:
    print('Ваша компания отработала в ноль.')
else:
    print(f'Ваша прибыль составила: {profit} рублей.')
    profitability = profit / revenue * 100
    print(f'Рентабельность компании: {profitability:.2f} %')
    staff = int(input('Сколько сотрудников работает в компании? '))
    staff_profit = profit / staff
    print(f'Прибыль компании в расчете на одного сотрудника составляет: {staff_profit:.2f} рублей.')