with open('task_5_1.txt', 'w', encoding=('utf-8')) as my_f:
    while True:
        st_wr = input('Напишите строку (для выхода нажмите Enter): ')
        if st_wr == '':
            break
        my_f.write(st_wr + '\n')