#!/usr/bin/env python
#coding=utf-8


def add(x,**kwargs):
    total = x
    for arg, value in kwargs.items():
        print "adding ", arg
        total += value
    return total

print add(10, y=11, z=12, w=13)

print "*"*80


def add(x, kwargs):
    total = x
    for arg, value in kwargs.items():
        print "adding ", arg
        total += value
    return total

input_dic={"y":11,"z":12,"w":13}
print add(10,input_dic)
