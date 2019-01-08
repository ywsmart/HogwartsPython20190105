#!/usr/bin/env python
#coding=utf-8

from appium import webdriver

desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '6.0'
desired_caps['deviceName'] = 'Android Emulator'
desired_caps['appPackage'] = 'com.android.browser'
desired_caps['appActivity'] = '.BrowserActivity'

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
driver.get("http://www.douban.com")