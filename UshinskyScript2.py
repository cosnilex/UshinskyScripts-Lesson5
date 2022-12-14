#!/usr/bin/python3
import functools
def func(*args):
    return functools.reduce((lambda x, y: x + y), args) #можно суммировать int,float,string,list,tuple и т.д
    """Использую модуль functools, который применяет 
    функцию reduce к элементам последовательности, 
    сводя её к единственному значению.
    functools.reduce(function, iterable)
    function = lambda x, y: x+y (функция, которую требуется применить к элементам последовательности)
    iterable = args (последовательность, элементы которой требуется свести к единственному значению)"""
try:
    print(f'{func(2,10,52,8,100.5)} ')
except UnboundLocalError:
     print(f'Введено ноль значений')
except TypeError:
    print(f'Введено ноль значений')
