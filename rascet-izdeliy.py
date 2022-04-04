izdelie1 = input('Название изделия: ')
cost1 = float(input(f'Расценка изделия {izdelie1}: '))
quantity1 = int(input(f'Количество изделий {izdelie1}: '))

izdelie2 = input('Название изделия: ')
cost2 = float(input(f'Расценка изделия {izdelie2}: '))
quantity2 = int(input(f'Количество изделий {izdelie2}: '))



suma = (cost1*quantity1 + cost2*quantity2)*0.6


print(f'{izdelie1} * {cost1} * {quantity1} + {izdelie2} * {cost2} * {quantity2} = {suma}')
