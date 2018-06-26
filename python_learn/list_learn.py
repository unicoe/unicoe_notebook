# -*- coding: utf-8 -*-
# @Time    : 18-6-24 下午10:12
# @Author  : unicoe
# @Email   : unicoe@163.com
# @File    : list_learn.py
# @Software: PyCharm Community Edition

x = [1,3,6,4,2,1,2,3]

y = x[:]

y.sort()

print(x)
print(y)

z = sorted(x)
print(z)

print [x*x for x in range(10)]

print [x*x for x in range(10) if x%3 ==0]

print [(x,y) for x in range(3) for y in range(3)]

def test_doc(x):
    """
    test doc
    :param x: 
    :return: 
    """
    return x

print test_doc.__doc__

class Secretive:

    def __inaccessible(self):
        print "bet you can't see me..."

    def accessible(self):
        print "The secret message is:"
        self.__inaccessible()

s =  Secretive()
s.accessible()

class Filter:
    def init(self):
        self.blocked = []
    def filter(self, sequence):
        return [x for x in sequence if x not in self.blocked]

class SPAMFilter(Filter):
    def init(self):
        self.blocked = ['SPAM']

f = Filter()
f.init()
print f.filter([1,2,3])

s = SPAMFilter()
s.init()
print s.filter(['SPAM','SPAM','SPAM','SPAM','SPAM','SPAM','test'])

print issubclass(SPAMFilter, Filter)

print SPAMFilter.__bases__


import exceptions


def MyExpectError(Exception):
    print "my expect Error"
    pass

try:
    x = 1
    y = 0
    print x/y
except ZeroDivisionError:
    pass
    #raise
else:
    print "other"
finally:
    print "clean up..."

class A:
    def hello(self):
        print "A"

class B(A):
    def hello(self):
        print "B"
    pass

a = A()
a.hello()
b = B()
b.hello()

__metaclass__ = type

class Bird:
    def __init__(self):
        self.hungry = True
    def eat(self):
        if self.hungry:
            print "aaa"
            self.hungry = False
        else:
            print "no"


bi = Bird()
bi.eat()

bi.eat()

class SongBird(Bird):
    def __init__(self):
        super(SongBird, self).__init__()
        self.sound = "squawk"
    def sing(self):
        print self.sound

sb = SongBird()
sb.sing()

sb.eat()

__metaclass__ = type

class Rectangle:
    def __init__(self):
        self.width = 0
        self.height = 0
    def setSize(self, size):
        self.width, self.height = size
    def getSize(self):
        return self.width, self.height
    size = property(getSize, setSize)

r = Rectangle()
r.width = 10
r.height = 5
print r.size


class Fibs:
    def __init__(self):
        self.a = 0
        self.b = 1
    def next(self):
        self.a , self.b = self.b, self.a+self.b
        if self.a > 1000: raise StopIteration
        return self.a
    def __iter__(self):
        return self

fibs = Fibs()
for f in fibs:
    if f > 1000:
        print f
        break

it = iter([1,2,3])
print it.next()
print it.next()

a =list(fibs)
print a

def flatten(nested):
    for sublist in nested:
        for element in sublist:
            yield  element

nested = [[1,2], [3,4], [5]]
for num in flatten(nested):
    print num

print list(flatten(nested))

def hello():
    print "hello world"
def test():
    hello()

if __name__ == '__main__': test()

import copy
print dir(copy)

print [n for n in dir(copy) if not n.startswith('_')]

print copy.__all__

print help(copy.copy)

print copy.__doc__


print range.__doc__

print copy.__file__

import sys

print sys.modules
print sys.path
print sys.platform
print sys.argv
print sys.stdin

import os
print os.environ
print os.system("pwd")
print os.sep
print os.pathsep
print os.linesep
print os.urandom(12)

import fileinput
print fileinput.input()

print fileinput.filename()

print set(range(10))
