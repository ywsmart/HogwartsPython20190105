#!/usr/bin/env python
#coding=utf-8

'''
for first_number in xrange(1,10):
    for second_number in xrange(1,first_number+1):
        print first_number,"*", second_number,"=",first_number*second_number,"",
    print "\n"
'''

wid=1
while wid <= 5:
    len=1
    while len <= wid:
        print "*","",
        len+=1
    print "\n"
    wid+=1
