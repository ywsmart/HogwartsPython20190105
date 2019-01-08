#!/usr/bin/env python
#coding=utf-8

from appium import webdriver
import time,sys

reload(sys)
sys.setdefaultencoding('utf-8')

usename="powertester@126.com"
passwd="123456@Fang"
sleep_time =2

desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '6.0'
desired_caps['deviceName'] = 'Android Emulator'
#desired_caps['app'] = r"D:\study\cy\training\ceba\code\src\appium\douban_117.apk"
desired_caps['appPackage'] = 'com.douban.frodo'
desired_caps['appActivity'] = '.MainActivity'

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

driver.find_element_by_android_uiautomator('new UiSelector().text("我的")').click()

time.sleep(sleep_time)
#driver.find_element_by_android_uiautomator('new Uiseletor().resourceId("com.douban.frodo:id/title").textContains(u"我的")').click()
driver.find_element_by_id("com.douban.frodo:id/unlongin_name").click()
time.sleep(sleep_time)

usename_element = driver.find_element_by_id("com.douban.frodo:id/input_user_name")
usename_element.clear()
usename_element.send_keys(usename)

password_element = driver.find_element_by_id("com.douban.frodo:id/input_password")
password_element.clear()
password_element.send_keys(passwd)

driver.find_element_by_id("com.douban.frodo:id/sign_in_douban").click()
time.sleep(sleep_time)
