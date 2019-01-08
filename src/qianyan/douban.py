#!/usr/bin/env python
# coding=utf-8

import requests

def login_douban(username, passwd):
    post_data = {'source': 'index_nav', 'form_email': username, 'form_password': passwd}
    request_headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko"}
    response = requests.post("http://www.douban.com/accounts/login", data=post_data, headers=request_headers)
    if u"powertester的帐号" in response.text:
        print "Login successful"
        return response
    else:
        print "Login failed"
        print response.text
        return False


def say_something(login_cookie):
    post_data = {'ck': 'ynNl', 'rev_title': u'发福利', 'rev_text': u'楼主是标题党', 'rev_submit': u'好了，发言'}
    response = requests.post("http://www.douban.com/group/beijing/new_topic", data=post_data, cookies=login_cookie)
    if response.url == "http://www.douban.com/group/beijing/":
        print "post new content successfully"
        return True
    else:
        print "Post content fail"
        return False

your_usename="powertester@126.com"
your_passwd="123456@Fang"
login_response = login_douban(your_usename, your_passwd)
say_something(login_response.cookies)

