#!/usr/bin/env python
#coding=utf-8


from appium import webdriver
import time,sys

reload(sys)
sys.setdefaultencoding('utf-8')


desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '6.0'
desired_caps['deviceName'] = 'Android Emulator'
#desired_caps['app'] = r"D:\study\cy\training\ceba\code\src\appium\douban_117.apk"
desired_caps['appPackage'] = 'com.android.contacts'
desired_caps['appActivity'] = '.activities.PeopleActivity'

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

aa = driver.find_element_by_android_uiautomator("new UiSelector().text('Create a new contact')")
print aa
#driver.find_elements_by_android_uiautomator("new UiSelector().resourceId('com.android.contacts:id/create_contact_button'')")
