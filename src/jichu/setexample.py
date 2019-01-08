#!/usr/bin/env python
#coding=utf-8

my_set = {1,2,3}
set1 = {4,5,6,1,10}
set2 = {4,5,6,1,3,"python"}

print my_set.union(set1)

print set2.difference(set1)

print set2.symmetric_difference(set1)
set2.discard(4)
print set2
set2.remove('java')
print set2