text = input('Напишите несколько слов через пробел: ')
for i, v in enumerate(text.split(), 1):
    print(f'{i}) {v}'[:13])