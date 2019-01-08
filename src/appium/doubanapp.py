#!/usr/bin/env python
#coding=utf-8

from appium import webdriver

desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '6.0'
desired_caps['deviceName'] = 'Android Emulator'
desired_caps['app'] = r"D:\study\cy\training\ceba\code\src\appium\douban_117.apk"
#print "000"
#desired_caps['browserName'] = 'Browser'
#desired_caps['appPackage'] = 'com.android.browser'
#desired_caps['appActivity'] = '.BrowserActivity'
print "111111111"
#try:
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
#except:
print "22222222"
#driver.install_app(r"D:\study\cy\training\ceba\code\src\appium\douban_117.apk")
import time
time.sleep(100)
