'''В прошлом модуле мы работали с системой оценок ECTS. 
Напишите функцию formatted_grades, которая принимает на вход словарь оценивания студентов
 по предмету следующего вида:

students = {"Nick": "A", "Olga": "B", "Mike": "FX", "Anna": "C"}
И возвращает список отформатированных строк, чтобы при выводе следующего кода:

for el in formatted_grades(students):
    print(el)
Получалась следующая таблица:

   1|Nick      |  A  |  5
   2|Olga      |  B  |  5
   3|Mike      | FX  |  2
   4|Anna      |  C  |  4
первый столбец — ширина 4 символа, выравнивание по правому краю
второй столбец — ширина 10 символов, выравнивание по левому краю
четвертый и пятый столбец — ширина 5 символов и выравнивание по центру
вертикальный символ | не входит в ширину столбца'''

grades = {"A": 5, "B": 5, "C": 4, "D": 3, "E": 3, "FX": 2, "F": 1}

students = {"Nick": "A", "Olga": "B", "Mike": "FX", "Anna": "C"}


def formatted_grades(students):
    count = 1
    result = []
    for key, value in students.items():
      if key and value:
        result.append('{:>4}|{:<10}|{:^5}|{:^5}'.format(
            count,  key,  value, grades.get(value)))
        count += 1
    return result


print(formatted_grades(students))