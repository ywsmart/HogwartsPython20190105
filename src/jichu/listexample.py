#!/usr/bin/env python
#coding=utf-8

my_list=["python", 12, 2.3, 9.7,10,9,19,60]
list2=[3,4,5]

print my_list+list2

print list2*3

lang = [["python", 0.4],["java",0.5]]

print my_list[1:3]

print my_list[-4:-2]
print my_list[::2]

print id(my_list)
del my_list[0]
print my_list
print id(my_list)

my_list2= my_list[0:]
print my_list2
print id(my_list2)

my_list.append("Java")
print  my_list

my_list.extend(list2)
print my_list

print my_list.pop()
print my_list

my_list.reverse()

print my_list

my_list3 =["a",95, 99]
my_list3.sort()
print my_list3

multiple_list = [[1,2],["a","b"],[1,2,4,5]]
print len(multiple_list)