name = input('Ваше имя? ')
surname = input('Ваша фамилия? ')
year = input('Год рождения? ')
city = input('В каком городе проживаете? ')
e_mail = input('Ваша электронная почта? ')
phone_number = input('Ваш номер телефона? ')
def user_data(name, surname, year, city, e_mail, phone_number):
    print(f'{surname} {name} из города {city}, родился в {year} году, номер телефона: {phone_number}, почта: {e_mail}.')
user_data(name, surname, year, city, e_mail, phone_number)