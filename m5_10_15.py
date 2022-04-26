'''Напишите функцию find_word, которая принимает два параметра: 
первый text и второй word. Функция выполняет поиск указанного слова word в тексте 
text с помощью функции search и возвращает словарь.

При вызове функции:

print(find_word("Guido van Rossum began working on Python in the late 1980s,
 as a successor to the ABC programming language, and first released it in 1991 
 as Python 0.9.0.", "Python"))
Результат должен быть следующего вида при совпадении:

{
    'result': True,
    'first_index': 34,
    'last_index': 40,
    'search_string': 'Python',
    'string': 'Guido van Rossum began working on Python in the late 1980s,
     as a successor to the ABC programming language, and first released it in 1991 as 
     Python 0.9.0.'
}
где

result — результат поиска True или False
first_index — начальная позиция совпадения
last_index — конечная позиция совпадения
search_string — часть строки, в которой было совпадение
string — строка, переданная в функцию
'''

import re

def find_word(text, word):
    dict = {}
    word = word.lower
    patern = rf"{word}"
    if re.search(patern, text):
         dict.get('result': 'True')
         span = text.span()
         dict.get('first_index': 'span'[0], 'last_index': 'span'[1])
         search_string = text.strint
         dict.get('search_string': search_string)
         string = string.group()
         dict.get('string': string)
    else:
         dict.get('result': False)
         dict.get('first_index': None, 'last_index': None)
         dict.get('search_string': word)
         dict.get('string': string)
    return dict
