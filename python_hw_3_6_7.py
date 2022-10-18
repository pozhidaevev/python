def chahge_text():
    text = input('Введите слова из маленьких латинских букв через пробел: ')
    text_ch = text.title() # для 6-го задания(для одного слова)  можно использовать метод capitalize
    return text_ch
print(chahge_text())