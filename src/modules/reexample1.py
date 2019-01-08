#!/usr/bin/env python
#coding=utf-8

# encoding: UTF-8
import re

# 将正则表达式编译成Pattern对象
pattern = re.compile(u'你好')

# 使用Pattern匹配文本，获得匹配结果，无法匹配时将返回None
match = pattern.match(u'你好，世界!')

print match
if match:
    # 使用Match获得分组信息
    print "result:",match.group()
