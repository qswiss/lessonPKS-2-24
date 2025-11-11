# Типы данных 
# int - целые числа
# set - множества, тип данных который так жеss как dict пишется через круглые скобки, только с исключением на то что они неупорядоченные и могут в себе хранить только уникальные значения
# tuple - кортеж (1, 2.3, 'hello4', [12,3,4,] 45) он абсолютно похож на списки, только с одним исключением, тем что он НЕ ИЗМЕНЯЕМЫЙ тип данных
# listA = [1, 2.3, 'hello', [12,3,4], 45]
# listA[2] = 'hello5ы'
# print(listA[2])

# tupleA = (1, 2, 3, 'hello4', [12,3,4],'hello4', 'hello4', 45)
# tupleA[2] = 'hello6'
# print(tupleA.count('hello4'))
# print(tupleA.index('hello4'))
# print(tupleA)

# setA = {'jiraf', 'Aibek', 'begemot', 'Gena'}
# setA = set(setA)
# print(type(setA))
# setA.add('Ninja')
# setA.remove('Aibek')
# setA.pop() 

listA = [1, 2.3, 'hello4', [12,3,4], 45, 'hello4', 'hello4', 'hello4']
listB = [1, 2.3, 'hello4', [12,3,4], 45]
listA.insert(2, 'Привет')
listA.pop(4)
listA.reverse()
print(listA.index('hello4'))
print(listA.count('hello4'))
listA.extend(listB)
print(listA)

# Переменные - variable
name = 'Marlen'
print(name)

# dict - dictionary - словари {key:value}
names_age = {
'elnura':18,
    'marsel':17,
    'marlen':17,
    'zahid':19,
    'aibike':16,
}
print(names_age.get('marlen')) # Выводит значения ключа
for itemkey, value in names_age.items():
    print(itemkey, value)