#!/usr/bin/env python
#coding=utf-8

my_dic={"name":"xiaozhang", "company":"baidu", "grade":"T7"}

dic2 = {"name":"xiaozhang", "company":"taobao", "grade":"P7"}

my_dic.update(dic2)

print my_dic["company"]

my_dic["sex"] = "Male"
my_dic["grade"] = "P9"
print my_dic

del my_dic["name"]
print my_dic
print my_dic.get("grade")
print my_dic.items()