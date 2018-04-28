#coding:utf-8
#LEGB
# L : Local 函数内部作用域
# E ： enclosing 函数内部与内嵌函数
# G ： global 全局作用域
# B ：build-in 内置作用域
# 装饰器和闭包

passline = 60 # G

def func(val):
    passline = 90 # L
    if val >= passline:
        print('pass')
    else:
        print('failed')
    def in_func(): #(val,)
        print(val)
    in_func()
    return in_func
def Max(val1,val2):
    return max(val1,val2)

f = func(89)
f() #in_func
print(f.__closure__)

print(Max(23,90))

#闭包

def func_150(val):
    passline = 90 # L
    if val >= passline:
        print('%d pass'%val)
    else:
        print('failed')
def func_100(val):
    passline = 60 # L
    if val >= passline:
        print('%d pass'%val)
    else:
        print('failed')

def set_passline(passline):
    def cmp(val):
        if val >= passline:
            print('%d pass'%val)
        else:
            print('failed')
    return cmp

f_100 = set_passline(60)
print(type(f_100))
print(f_100.__closure__)
f_150 = set_passline(90)
f_100(89)
f_150(89)

func_100(89)
func_150(89)

# 封装 和 代码复用
def my_sum(*arg):
    if len(arg) == 0:
        return 0
    for val in arg:
        if not isinstance(val,int):
            return 0
    return sum(arg)
def my_average(*arg):
    if len(arg) == 0:
        return 0
    for val in arg:
        if not isinstance(val,int):
            return 0
    return sum(arg)/len(arg)

print(my_sum(1,2,3,4,5))
print(my_sum(1,2,3,4,5,'6'))
print(my_average(1,2,3,4,5))
print(my_average())


def dec(fun):
    def in_dec(*arg):
        print('in dec arr = ', arg)
        if len(arg) == 0:
            return 0
        for val in arg:
            if not isinstance(val, int):
                return 0
        return fun(*arg)
    return in_dec

def my_sum(*arg):
    print('in my_sum',arg)
    return sum(arg)
def my_average(*arg):
    print('in average',arg)
    return sum(arg) / len(arg)

# dec return in_dec -> my_sum
#my_sum = in_dec(*arg)
my_sum = dec(my_sum)
my_average = dec(my_average)

print(my_sum(1,2,3,4,5))
print(my_sum(1,2,3,4,5,'6'))
print(my_average(1,2,3,4,5))
print(my_average())


# 装饰器
def dec(fun):
    print('call dec')
    def in_dec(*arg):
        print('in_dec arr = ', arg)
        if len(arg) == 0:
            return 0
        for val in arg:
            if not isinstance(val, int):
                return 0
        return fun(*arg)
    return in_dec

@dec
def my_sum(*arg):
    print('in my_sum',arg)
    return sum(arg)

@dec
def my_average(*arg):
    print('in average',arg)
    return sum(arg) / len(arg)

print(my_sum(1,2,3,4,5))
print(my_average(1,2,3,4,5))

def deco(func):
    def in_deco():
        print('in deco')
        func()
    print('call deco')
    return in_deco
@deco
def bar(x,y):
    print('in bar',x+y)
print(type(bar))
bar(1,2)
