#!/usr/bin/python
#-*- conding:UTF-8 -*-

#面向对象 类 （属性和方法） 和 对象（个体）
#多态  同一类人对不同的事情也有不同的看法  重写父类
#封装性  包装了
#继承性  继承来自父类的方法  单继承 多继承
# 构造函数  析构函数  老式类和新式类

#

class OldStyle:
    def __init__(self,name,description):
        self.name = name
        self.description = description

class NewStyle(object):
    def __init__(self,name,description):
        self.name = name
        self.description = description

if __name__ == '__main__':
    old = OldStyle('old','old style class')
    print(old)
    print(type(old))
    print(dir(old))
    print('----------------------')

    new = NewStyle('new','New style class')
    print(new)
    print(type(new))
    print(dir(new))

#  访问控制
# _ 私有属性

class Programer:
    hobby = 'Play computer'

    def __init__(self,name,age,weight):
        self.name = name
        self._age = age
        self.__weight = weight

    def get_weight(self):
        return self.__weight

if __name__ == '__main__':
    programer = Programer('Albert',25,80)
    print('dir(programer)#列举属性\n')
    print(dir(programer))
    print('programer.__dict__#字典形式输出\n')
    print(programer.__dict__)
    print('programer.get_weight()函数中取值\n')
    print(programer.get_weight())
    print('programer._Programer__weight属性方法访问\n')
    print(programer._Programer__weight)

#方法的定义
#装饰器  @classmethad  @property

class Programer:
    hobby = 'Play computer'

    def __init__(self, name, age, weight):
        self.name = name
        self._age = age
        self.__weight = weight

    @classmethod
    def get_hobby(cls):
        return cls.hobby

    @property
    def get_weight(self):
        return self.__weight

    def self_instroduction(self):
        print('My name is %s \nI am %s years old\n' %(self.name,self._age))

if __name__ == '__main__':
    programer = Programer('Albert', 25, 80) #实例化对象
    print('dir(programer)#列举属性\n')
    print(dir(programer))
    print('Programer.get_hobby()# @classmethod方法输出\n')
    print(Programer.get_hobby())
    print('programer.get_weight  @property 函数中取值 没有()\n')
    print(programer.get_weight)
    print('programer.self_instroduction()直接调用方法输出\n')
    programer.self_instroduction()

#继承

class Programer:
    hobby = 'Play computer'

    def __init__(self, name, age, weight):
        self.name = name
        self._age = age
        self.__weight = weight

    @classmethod
    def get_hobby(cls):
        return cls.hobby

    @property
    def get_weight(self):
        return self.__weight

    def self_instroduction(self):
        print('My name is %s \nI am %s years old\n' %(self.name,self._age))

class BackendProgramer(Programer):

    def __init__(self,name,age,weight,language):
        super(BackendProgramer, self).__init__(name,age,weight) #super 父类
        self.language = language


if __name__ == '__main__':
    programer = BackendProgramer('Albert', 25, 80,'Python') #实例化对象
    print('dir(programer)#列举属性\n')
    print(dir(programer))
    print('programer.__dict__#字典形式输出\n')
    print(programer.__dict__)
    print('type(programer)# 输出对象类型\n')
    print(type(programer))
    print('isinstance(programer,Programer) 判断是不是父类\n')
    print(isinstance(programer,Programer))

#多态  继承和方法的重写
class Programer:
    hobby = 'Play computer'

    def __init__(self, name, age, weight):
        self.name = name
        self._age = age
        self.__weight = weight

    @classmethod
    def get_hobby(cls):
        return cls.hobby

    @property
    def get_weight(self):
        return self.__weight

    def self_instroduction(self):
        print('My name is %s \nI am %s years old\n' %(self.name,self._age))

class BackendProgramer(Programer):

    def __init__(self,name,age,weight,language):
        super(BackendProgramer, self).__init__(name,age,weight) #super 父类
        self.language = language

    def self_instroduction(self):
        print('My name is %s \nMy favorite language is %s' %(self.name,self.language))

def introduce(programer):
    if isinstance(programer,Programer):
        programer.self_instroduction()


if __name__ == '__main__':
    programer = Programer('Albert', 25, 80)
    backend_programer = BackendProgramer('Tim', 30, 70,'Python') #实例化对象
    print('introduce(programer)#\n')
    introduce(programer)
    print('introduce(backend_programer)#\n')
    introduce(backend_programer)

# Magic Method 有前后下划线的
#__new__ ,__init__

class Programer:
    def __new__(cls, *args, **kwargs):
        print('call__new__method')
        print(args)
        return super(Programer,cls).__new__
    def __init__(self,name,age):
        print('call__init__method')
        self.name = name
        self.age = age

if __name__ == '__main__':
    programer = Programer('Min',24)
 #   print(programer.__dict__)  AttributeError:

 #运算符  __cmp/eq/it/gt__  __add/sub/mul/div__  __or/and__

class Programer():

    def __init__(self,name,age):
        self.name = name
        if isinstance(age,int):
            self.age = age
        else:
            raise Exception('age must be int')

    def __eq__(self, other):
        if isinstance(other,Programer):
            if self.age == other.age:
                return True
            else:
                return False
        else:
            raise Exception('The type of object must be Programer')

    def __add__(self, other):
        if isinstance(other,Programer):
            return self.age + other.age
        else:
            raise Exception('The Type of object must be Programer')
if __name__ == '__main__':
    p1 = Programer('alb',25)
    p2 = Programer('Min',24)
    print(p1 == p2)
    print(p1 + p2)

#类的展现
# __str/repr/unicode__

class Programer():

    def __init__(self,name,age):
        self.name = name
        if isinstance(age,int):
            self.age = age
        else:
            raise Exception('age must be int')

    def __str__(self):
       return '%s is %s years old' %(self.name,self.age)
    def __dir__(self):
       return self.__dict__.keys()

if __name__ == '__main__':
    p = Programer('min',24)
    print(p)
    print(dir(p))


# 无限递归
class Programer():

    def __init__(self,name,age):
        self.name = name
        if isinstance(age,int):
            self.age = age
        else:
            raise Exception('age must be int')
    def __getattribute__(self, name):
        #return getattr(self,name)
        #return self.__dict__[name]
        return super(Programer,self).__getattribute__(name)

    def __setattr__(self, name, value):
        #setattr(self,name,value)
        self.__dict__[name] = value

if __name__ == '__main__':
    p = Programer('min',24)
    print(p.name)
















