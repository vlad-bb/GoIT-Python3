'''В компании существует несколько отделов. Список сотрудников для каждого отдела имеет такой вид:

['Robert Stivenson,28', 'Alex Denver,30']
Это список строк с фамилией и возрастом сотрудника, разделенными запятыми.

Реализуйте функцию записи данных о сотрудниках компании в файл, 
чтобы информация о каждом сотруднике начиналась с новой строки.

Функция записи в файл write_employees_to_file(employee_list, path), где:

path - путь к файлу.
employee_list - список со списками сотрудников по каждому отделу, как в примере ниже:
[['Robert Stivenson,28', 'Alex Denver,30'],['Drake Mikelsson,19']]
Требования:

запишите содержимое employee_list в файл, используя режим "w".
мы пока не используем менеджер контекста with
каждый сотрудник должен быть записан с новой строки — т.е для предыдущего списка содержимое файла
 должно быть следующим:
Robert Stivenson,28
Alex Denver,30
Drake Mikelsson,19'''

import pathlib

def write_employees_to_file(employee_list, path):
    global_employee_list = open('path', 'w')
    for i in employee_list:
        global_employee_list.write(i)
        global_employee_list.write('\n')
    global_employee_list.close()



