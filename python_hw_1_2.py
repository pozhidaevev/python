a = int(input('Введите время в секундах (не больше чем 86400): '))

hours = a // 3600
balance = a % 3600
minutes = balance // 60
seconds = balance % 60

if hours < 10:
    hours = '0' + str(hours)
if minutes < 10:
    minutes = '0' + str(minutes)
if seconds < 10:
    seconds = '0' + str(seconds)

print(f'{hours}:{minutes}:{seconds}')

