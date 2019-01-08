#!/usr/bin/env python
#coding=utf-8

def sqr(x):
    return x ** 2

a = [4,5,8]

print map(sqr, a)

my_list = []
for a_item in a:
    my_list.append(sqr(a_item))

print my_list