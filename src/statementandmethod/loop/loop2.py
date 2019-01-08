#!/usr/bin/env python
#coding=utf-8

companys = ['google', 'baidu',  'aili',"taobao"]

for company in companys:
    print company
    if company == "google":
        print "google 是个不作恶的公司"
    elif company == "baidu":
        print "中国搜索公司"
    else:
        print "非搜索引擎公司"