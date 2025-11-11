# *args, **kwargs
# arguments

def add(*args):
    print(args)

add(7,8,5,6,7,89)

a = [5,6,7,8,9]
b = [1,2,*a,3,4]
print(b)

def sum2(*args):
    total = 0
    for n in args:
        total+=n
    print(f"Сумма: {total}")

sum2(4,5,5,6,7,8,9,0,5,6,7,90)

def printScore(student, *args):
    print(f"Имя: {student}")
    for sc in args:
        print(f"{sc}: end=', '")
print("Мао", 2,2,3,4,3,2)

def show(**kwargs):
    for k,v in kwargs.items():
        print(f"{k}: {v}")

show(name='Mao', age=17, birth='12.12.2000')

def pets(owner, **kwargs):
    print(f"Хозяин: {owner}")
    for k, v in kwargs.items():
        print(k, v)

pets('Zahid', dog='Bobik', cat='Bruda', eats=('fish', 'meat', 'water'))

# КОМБИНАЦИЯ

def demo(a, *args, **kwargs):
    print('a=',a)
    print('args=',args)
    print('kwargs=',kwargs)

demo(43, 3,4,5,6,7,56,7,8,9, age=45, hobbi='гимнастика', phone='redmi')