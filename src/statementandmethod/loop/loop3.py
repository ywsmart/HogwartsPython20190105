#!/usr/bin/env python
#coding=utf-8

companys = ['google', 'baidu',  'aili',"taobao"]

for index in xrange(len(companys)):
    print companys[index]
    if companys[index] == "google":
        print "google 是个不作恶的公司"
    elif companys[index] == "baidu":
        print "中国搜索公司"
    else:
        print "非搜索引擎公司"
        
