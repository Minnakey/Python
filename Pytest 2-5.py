# 检查成员资格

permissions = 'minnakey'

if 'min' in permissions : print('yes')

user = ['minnakey','roller','jane']
name = input('Please input the username: ')

if name in user : print('this is a correct username!')

# 最大值、最小值、长度

numbers = [100,34,678]
l = len(numbers)
ma = max(numbers)
mi = min(numbers)

print( l+ma+mi)

# list test

lst = [1,2,3,4,5,6]

lst.append(7)
lst2 = lst
lst3 = lst.copy()
print(lst)
print(lst2.count(1))

lst.extend(lst2)
print(lst)

lst2.reverse()
print(lst2)

lst2.clear()
lst3.clear()
print(lst3)
print(lst2)
print(lst)


