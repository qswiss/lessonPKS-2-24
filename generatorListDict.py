# Генератор списков
data = []
for i in range(100):
    if i % 2 ==0:
        data.append(i)
print(data)
# Генератор списков - list comprehension
data2=[i for i in range(100)]
print(data2)
######## dict comprehension
marks = {
    'gena':40,
    'alla':50,
    'bini':30,
}
newMarks = [v, for k,v in marks.items()]
print(newMarks)


my_str = "frghfkiuwejdhciow65"
nums = []
for i in my_str:
    if i.isdigit():
        temp+=i
    elif temp:
        nums.append(int(temp))
        temp = ''
print(nums)