str_en = 'abracadabra'
str_ru = 'абракадабра'

bytes_en = str_en.encode(encoding='WINDOWS-1251')
bytes_ru = str_ru.encode(encoding='WINDOWS-1251')

print(bytes_en)
print(bytes_ru)

print('Обратное преобразование')
print(bytes_en.decode(encoding='WINDOWS-1251'))
print(bytes_ru.decode(encoding='WINDOWS-1251'))
