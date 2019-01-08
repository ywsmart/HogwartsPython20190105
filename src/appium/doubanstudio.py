#!/usr/bin/env python
#coding=utf-8

import unittest
import time
from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions


class Untitled(unittest.TestCase):
    reportDirectory = 'reports'
    reportFormat = 'xml'
    dc = {}
    testName = 'Untitled'
    driver = None

    def setUp(self):
        self.dc['reportDirectory'] = self.reportDirectory
        self.dc['reportFormat'] = self.reportFormat
        self.dc['testName'] = self.testName
        self.dc['udid'] = '192.168.31.101:5555'
        self.dc['deviceName'] = 'Android Emulator'
        self.dc['appPackage'] = 'com.douban.frodo'
        self.dc['appActivity'] = '.activity.SplashActivity'
        self.dc['platformName'] = 'android'
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', self.dc)

    def testUntitled(self):
        time.sleep(30)
        print "waiting"
        self.driver.find_element_by_xpath("xpath=//*[@id='icon' and ./parent::*[@id='icon_layout' and ./following-sibling::*[@text='我的']]]").click()
        self.driver.find_element_by_xpath("xpath=//*[@text='登录 / 注册']").click()
        self.driver.find_element_by_xpath("xpath=//*[@id='input_user_name']").click()
        self.driver.execute_script("client:client.sendText(\"powertester@126.com\")")
        self.driver.find_element_by_xpath("xpath=//*[@id='input_password']").send_keys('123456yin')
        self.driver.find_element_by_xpath("xpath=//*[@text='登录']").click()

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
        unittest.main()
