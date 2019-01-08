#!/usr/bin/env python
#coding=utf-8

import random
def fast_sorted(L):
    if len(L) < 2: return L
    pivot_element =random.choice(L)
    print pivot_element
    small = [i for i in L if i < pivot_element]
    medium = [i for i in L if i == pivot_element]
    large = [i for i in L if i > pivot_element]
    return fast_sorted(small) + medium + fast_sorted(large)


#print fast_sorted([7,4,5,7,8,2,1])

#1,1,2,3,5,8,13
def fib(num):
    if isinstance(num,int):
        if num > 0:
            res = [1]
            if num <= 1:
                return [1]
            else:
                for i in xrange(1,num):
                    res.append(i)
                    res.append(res[i]+i)
    else:
        return False

