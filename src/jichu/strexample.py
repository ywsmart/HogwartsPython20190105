#!/usr/bin/env python
#coding=utf-8


path='-rw-r--r--    1 root root   182 Nov  6 23:31 month.py'

list1= path.split()
#print list1[-4:]


love="I love Java"
print love.replace("Java","Python")

print love.upper()
print love.lower()

print "i love Java".capitalize()

print love.startswith("i")

list1 =["I","love","Python"]
print " ".join(list1)

print love.index("va")