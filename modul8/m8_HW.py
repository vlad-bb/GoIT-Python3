''' Вам нужно реализовать полезную функцию для вывода списка коллег,
которых надо поздравить с днём рождения на неделе.

У вас есть список словарей users, каждый словарь в нём обязательно имеет ключи name и birthday.
Такая структура представляет модель списка пользователей с их именами и днями рождения.
name — это строка с именем пользователя, а birthday — это datetime объект, в котором записан день рождения.
Ваша задача написать функцию get_birthdays_per_week,
которая получает на вход список users и выводит в консоль (при помощи print) список пользователей,
которых надо поздравить по дням.
Условия приёмки#
get_birthdays_per_week выводит именинников в формате:
Monday: Bill, Jill
Friday: Kim, Jan
Пользователей, у которых день рождения был на выходных, надо поздравить в понедельник.
Для отладки удобно создать тестовый список users и заполнить его самостоятельно.
Функция выводит пользователей с днями рождения на неделю вперед от текущего дня.
Неделя начинается с понедельника. '''

from datetime import datetime, timedelta

users = [
    {"name": "Vladyslav", "birthday": "22 May 1990"},
    {"name": "Elena", "birthday": "16 May 1990"},
    {"name": "Ludmila", "birthday": "16 May 1990"},
    {"name": "Tatyana", "birthday": "12 March 1965"},
]


def get_birthdays_per_week(users):
    start = datetime.now().date()
    end = start + timedelta(days=7)
    for i in users:
        birthday = datetime.strptime(i["birthday"], "%d %B %Y")
        date_b = datetime(start.year, birthday.month, birthday.day)
        if start <= date_b.date() <= end:
            day = date_b.weekday()
            if day == 0:
                print("Monday: " + i["name"])
            if day == 1:
                print("Tuesday: ", +i["name"])
            if day == 2:
                print("Wednesday: " + i["name"])
            if day == 3:
                print("Thursday: " + i["name"])
            if day == 4:
                print("Friday: " + i["name"])
            if day in (5, 6):
                print('Next Monday: ' + i['name'])
            if day not in (0, 1, 2, 3, 4, 5, 6):
                print("No birthday in this week")


get_birthdays_per_week(users)








