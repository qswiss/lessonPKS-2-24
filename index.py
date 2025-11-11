name = 'Elnura'
prof = 'student'
age = 18
# конкатенция строк (сложение строк) с помощью +
bio = 'I am'+name+','+str(age)+'years, I am a'+prof
print(bio)
# форматирование строк с помощью f-строк
bio2 = f'I am {name}, {age} years, I am a {prof}'
print(bio2)
# форматирование строк с помощью метода format
bio = 'I am {0}, {1} years, I am a {2}'.format(name, age, prof)
print(bio)

# индексы это порядковый номер символа в строке
# индексы начинаются с 0
name = 'Elnura Abdullaeva Rashidovna'
print(name[7],name[8],name[9],name[10],name[11],name[12],name[13],name[14])

# срезы строк (substring) [start:stop:step]
print(name[0:6]) # с 0 индекса по 6 не включая
print(name[7:17]) # с 7 по 17 не включая
print(name[0:14:2]) # шаг 2
print(name[:6]) # с начало по 6 не включая
print(name[::-1]) # реверс строки 

age - input('Введите ваш возраст: ')
age - int(age) # преобразование строки в целое число
if age >0 and age < 16:
 print('Пока рано')
elif age >= 16 and age < 18:
 print('Готовься на службу')
elif age >= 18 and age <= 45:
 print('Идем служить')
elif age > 45 and age <= 60:
 print('Пора на пенсию')
elif age > 60 and age <= 100:
 print('Отдыхай')
else:
 print('Ошибка введите возраст корректно')