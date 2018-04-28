#!/usr/bin/python
# -*- coding: utf-8 -*-

a = 45678
b = 0x12fd2 # 16
s = a+b

print(s)

print('Learn Python in imooc')

x = 100< 99 #False

print(x)

y = 0xff == 255 #True

print(y)


#Hello,Python

#input code
print('Hello,Python')
print("Hello,Python")
print('hello')
print ('Pyhon')

x1 = 1
d = 3
n = 100
x100 = x1+(n-1)*d
s = (x1+x100)*n/2

print(s)

s = 'Python was started in 1989 by \"Guido\".\n Python is free and easy to learn.'
print(s)

print (r'''"To be,or not to be": that is the question.
Whether it's nobler in the mind to suffer.''')

print (u'''静夜思
床前明月光，
疑是地上霜。
举头望明月，
低头思故乡。''')

print(2.5 + 10%4 )
print(2.5 + 10.0/4 )

a = 'python'
print ('hello,', a or 'world')

b = ''
print ('hello,', b or 'world')

#List [] []  appent insert pop
L = ['Adam', 95.5, 'Lisa', 85, 'Bart', 59]
print (L)

L = [95.5,85,59]
print (L[0])
print (L[1])
print (L[2])
#print (L[3])
print (L[-1])
print (L[-2])
print (L[-3])

L = ['Adam', 'Lisa', 'Bart']
L.append('Minnakey')
L.insert(2,'Paul')
print (L)

L = ['Adam', 'Lisa', 'Paul', 'Bart']
L.pop(2)
L.pop(2)
print (L)

L = ['Adam', 'Lisa', 'Bart']
L[0] = 'Bart'
L[-1] = 'Adam'
print (L)

#tuple () () 元组元素数量不可变
t = (0,1,2,3,4,5,6,7,8,9)
print (t)

#包含 0 个元素的 tuple，也就是空tuple，直接用 ()表示：
t = ()
print(t)
#创建单元素
t = (1,)
print(t)
#“可变”的tuple
t = ('a', 'b', ['A','B'])
print (t)
t = ('a', 'b', ('A','B'))
print (t)

# if ::::: else :::::  elif ::::;
score = 75
if score >= 60:
    print ('passed')

score = 55
if score >= 60:
    print ('passed')
else:
    print ('failed')

score = 85
if score >= 90:
    print ('excellent')
elif score >= 80:
    print ('good')
elif score >= 60:
    print ('passed')
else:
    print ('failed')

# for for循环体（就是缩进的代码块）。
L = [75, 92, 59, 68]
sum = 0.0
for score in L:
    sum = sum + score
print (sum / 4)

# while
sum = 0
x = 1
while x < 100:
    sum = sum + x
    x = x +2
print (sum)

#  while true + break
sum = 0
x = 1
n = 1
while True:
    sum = sum + x
    x = x*2
    n = n+1
    if n >20:
       break
print (sum)

##对已有的计算 0 - 100 的while循环进行改造，通过增加 continue 语句，使得只计算奇数的和：
sum = 0
x = 0
while True:
    x = x + 1
    if x > 100:
        break
    if x % 2 == 0:
        continue
    sum = sum + x

print (sum)

#对100以内的两位数，请使用一个两重循环打印出所有十位数数字比个位数数字小的数，
for x in [1,2,3,4,5,6,7,8,9]:
    for y in [0,1,2,3,4,5,6,7,8,9]:
        if x< y :
            print (x*10 + y)

#dict  value key
d = {
    'Adam': 95,
    'Lisa': 85,
    'Bart': 59,
    'Paul': 75
}
print (len(d))

#dir {}
d = {
    'Adam': 95,
    'Lisa': 85,
    'Bart': 59
}
print ('Adam:',d['Adam'])
print ('Lisa:',d['Lisa'])
print ('Bart:',d['Bart'])

# 加入一个dir
d = {
    95: 'Adam',
    85: 'Lisa',
    59: 'Bart'
}
d[72] = 'Paul'

#遍历dir
d = {
    'Adam': 95,
    'Lisa': 85,
    'Bart': 59
}
for name in d:
    print (name + ':',d[name])

### set  访问 set中的某个元素实际上就是判断一个元素是否在set中。 set 中是List 但没有重复数
s = set(['Adam','Lisa','Bart','Paul'])

months = set(['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'])
x1 = 'Feb'
x2 = 'Sun'

if x1 in months:
    print (x1 + ': ok')
else:
    print (x1 + ': error')

if x2 in months:
    print (x2 + ': ok')
else:
    print (x2+ ': error')

s = set([('Adam', 95), ('Lisa', 85), ('Bart', 59)])
for x in s:
    print (x[0] + ':' , x[1])   #
   # print (x[0] + ':' + x[1])   # TypeError: must be str, not int

s = set(['Adam', 'Lisa', 'Paul'])
L = ['Adam', 'Lisa', 'Bart', 'Paul']
for name in L:  # for 是遍历list if 不可以
    if name in s:
        s.remove(name)
    else:
        s.add(name)
print (s)

#sum()函数接受一个list作为参数，并返回list所有元素之和。请计算 1*1 + 2*2 + 3*3 + ... + 100*100。
import math
L = []
x = 1
while x <= 100:
    L.append( x*x )
    x = x + 1
print (L)
#print (sum(L),0)

#自定义函数
def square_of_sum(L):
    sum = 0
    for n in L:
        sum = sum + n*n
    return sum

print (square_of_sum([1, 2, 3, 4, 5]))
print (square_of_sum([-5, 0, 5, 15, 25]))

#函数返回多值
import math

def quadratic_equation(a, b, c):
    t = math.sqrt(b*b-4*a*c)
    return (-b+t)/(2*a),(-b-t)/(2*a)

print (quadratic_equation(2, 3, 0))
print (quadratic_equation(1, -6, 5))

#递归函数



#定义默认参数
print(int('123',4))

def greet(name='world'):
    print ('Hello,'+ name + '.')

greet()
greet('Bart')

#定义可变参数 def fn(*args)
def average(*args):
    sum = 0.0
    if len(args) == 0:
        return sum
    for x in args:
        sum = sum + x
    return sum/len(args)

print (average())
print (average(1, 2))
print (average(1, 2, 2, 3, 4))

#对List进行切片
#range()函数可以创建一个数列：
#请利用切片，取出：
L = range(1,101)

print(L[:10])  #1. 前10个数；
print(L[2::3])  #2. 3的倍数；
print(L[4:50:5])  #3. 不大于50的5的倍数。

print(L[-10:]) #最后10个数
print(L[-46::5]) #最后10个5的倍数

#但它会把所有字母都变成大写。请设计一个函数，它接受一个字符串，然后返回一个仅首字母变成大写的字符串。
def firstCharUpper(s):
    return s[:1].upper()+s[1:]

print (firstCharUpper('hello'))
print (firstCharUpper('sunday'))
print (firstCharUpper('september'))

#迭代（Iteration）
for i in range(1,101):
    if i % 7 == 0:
        print(i)

#迭代永远是取出元素本身，而非元素的索引。
#在迭代 ['Adam', 'Lisa', 'Bart', 'Paul'] 时，如果我们想打印出名次 - 名字（名次从1开始)，请考虑如何在迭代中打印出来
#zip()函数可以把两个 list 变成一个 list
L = ['Adam', 'Lisa', 'Bart', 'Paul']
for index, name in zip(range(1,len(L)+1),L):
    print (index, '-', name)

#dict values()  itervalues()
#d = { 'Adam': 95, 'Lisa': 85, 'Bart': 59, 'Paul': 74 }
#sum = 0.0
#for v in d.itervalues():
#    sum = sum + v
#print (sum/len(d))

#d = { 'Adam': 95, 'Lisa': 85, 'Bart': 59, 'Paul': 74 }

#sum = 0.0
#for k, v in d.iteritems():
    #    sum = sum + v
#        print (k,':',v)
#print ('average', ':', sum/len(d))


print([x*(x+1) for x in range(1,100,2)])


d = { 'Adam': 95, 'Lisa': 85, 'Bart': 59 }
def generate_tr(name, score):
    if score < 60:
        return '<tr><td>%s</td><td style="color:red">%s</td></tr>' % (name, score)
    return '<tr><td>%s</td><td>%s</td></tr>' % (name, score)
try:
    tds = [generate_tr(name, score) for name, score in d.iteritems()]
except AttributeError:
    print("AttributeError")
else:
    print('correct')

print ('<table border="1">')
print ('<tr><th>Name</th><th>Score</th><tr>')
try:
    print ('\n'.join(tds))
except NameError:
    print('name error')

print ('</table>')

#请编写一个函数，它接受一个 list，然后把list中的所有字符串变成大写后返回，非字符串元素将被忽略。

#1. isinstance(x, str) 可以判断变量 x 是否是字符串；
#2. 字符串的 upper() 方法可以返回大写的字母。

def toUppers(L):
    return [x.upper() for x in L if isinstance(x,str)]

print (toUppers(['Hello', 'world', 101]))

#利用 3 层for循环的列表生成式，找出对称的 3 位数。例如，121 就是对称数，因为从右到左倒过来还是 121。
print([100*n1 + 10*n2 + n3 for n1 in range(10) for n2 in range(10) for n3 in range(10) if n1==n3])
