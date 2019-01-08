#!/usr/bin/env python
#coding=utf-8

def add_method(x,y):
    '''
    :param x:
    :param y:
    :return: value or None if one of parameter is not digit
    '''
    try:
        return x+y
    except Exception,e:
        print e
        return None

#print add_method(10,11)

