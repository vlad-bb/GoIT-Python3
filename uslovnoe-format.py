from unicodedata import name


zarplata = input('Ckolko tu zarabatuvaesh v mesyac?:')
zarplata = int(zarplata)

if zarplata > 10000:
    print('Normalno')
elif zarplata < 10000:
    print('Malo')
else:
    print('Ne ponyatno')

