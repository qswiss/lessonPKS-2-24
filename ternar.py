is_fast = True
if is_fast:
    car = 'Ferrari'
else:
    car = 'Tico'
print(car)
#### Тернарный оператор
car2 = 'BMW' if is_fast else 'Matiz'
########
a, b, c = 45, 56, 79 # множественное присвоение
max2 = a if a>b and a>c else b if b>c else c
print(max2)