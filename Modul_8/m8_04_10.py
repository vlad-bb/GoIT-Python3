''' Для того чтобы выиграть главный приз лотереи,
необходимо совпадение нескольких номеров на лотерейном билете с числами,
выпавшими случайным образом и в неком диапазоне во время очередного тиража.
Например, необходимо угадать шесть чисел от 1 до 49 или пять чисел от 1 до 36 и т.д.

Напишите функцию, которая будет случайным образом подбирать набор чисел для лотерейного билета.
Среди этих чисел не должно быть дубликатов.

Формат функции get_numbers_ticket(min, max, quantity), где параметры:

min — минимальное значение диапазона, не может быть меньше 1
max — максимальное значение диапазона, не может быть большее 1000
quantity — количество чисел в наборе (должен быть min < quantity < max)
Функция должна вернуть список случайных чисел по возрастанию.
Если нарушены условия ограничений на параметры функции, тогда вернуть пустой список. '''
import random
from random import randrange


def get_numbers_ticket(min, max, quantity):
    result = []
    if min > 0 and max <= 1000 and min < quantity < max:
        for i in range(quantity):
            i = randrange(min, max+1)
            if i not in result:
                result.append(i)
                result.sort()
            if i in result:
                quantity += 1
        return result
    else:
        return result

print(get_numbers_ticket(1, 36, 5))
