#!/usr/bin/env python
#coding=utf-8

import requests
import sys

login_home_url="https://passport.csdn.net/account/login?ref=toolbar"
csdn_sessions= requests.Session()
response = csdn_sessions.get(login_home_url)
print response.text
#print response.text.find('name="lt"')
#print response.text.find("/>",response.text.find('name="lt"'))
lt_sting = response.text[response.text.find('name="lt"'): response.text.find("/>",response.text.find('name="lt"'))]
print lt_sting
print "*"*30
lt =  lt_sting[lt_sting.find("LT"):-2]
print lt
exe_sting = response.text[response.text.find('name="execution"'): response.text.find("/>",response.text.find('name="execution"'))]

execution =exe_sting[exe_sting.rfind('="')+2:-2]
print execution


payload ={"gps":"","username":"powerccna","password":"123456@Fang","rememberMe":"true","lt":lt,"execution":execution,"_eventId":"submit"}
headers= {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36","Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
          "Accept-Encoding": "gzip, deflate, br","Accept-Language": "en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7"}
login_url = "https://passport.csdn.net/account/verify"
login_response = csdn_sessions.post(login_url,data = payload, headers =headers)
print login_response.text

print "&"*20
comment_url = "http://blog.csdn.net/powerccna/comment/submit?id=8038904"
comment_headers= {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko","Accept": "*/*"}
comment_payload ={"commentid":"","content":u"早日完成！很期待！！","replyId":""}
comment_response = csdn_sessions.post(comment_url,data = comment_payload, headers =comment_headers)
print comment_response.text

