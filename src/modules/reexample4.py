#!/usr/bin/env python
#coding=utf-8


import re

p = re.compile(r'\d+')
#print p.split('one1two2three3four4')
print p.findall('one1two2three3four4')

