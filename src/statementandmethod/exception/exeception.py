#!/usr/bin/env python
#coding=utf-8


def expectionalexample(x,y):
    try:
        result = x / y
    except ZeroDivisionError:
        print "除数不能为0"
    #except Exception, e:
    #    print e
    else:
        print "结果是", result
    finally:
        print "任何情况下都有我的存在"



expectionalexample(10,5)

'''
def read_file(in_file):
    try:
        file_in = open(in_file,"r")
    except IOError,e:
        print e

read_file("../loop/loop1.py1")
'''

