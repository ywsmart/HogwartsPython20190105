#!/usr/bin/env python
# coding=utf-8

from selenium import webdriver
import unittest, time, re


class WeiboTestCase(unittest.TestCase):
    def setUp(self):
        print "2222"
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_untitled_test_case(self):
        driver = self.driver
        print "i ma here"
        driver.get("https://weibo.com/login.php")
        driver.find_element_by_id("loginname").click()
        driver.find_element_by_id("loginname").click()
        driver.find_element_by_id("loginname").clear()
        driver.find_element_by_id("loginname").send_keys("xxxxx")
        driver.find_element_by_name("password").clear()
        driver.find_element_by_name("password").send_keys("xxxx")
        driver.find_element_by_id("login_form_savestate").click()
        driver.find_element_by_xpath("//div[@id='pl_login_form']/div/div[3]/div[6]/a").click()
        driver.find_element_by_xpath("//textarea[@name='']").clear()
        driver.find_element_by_xpath("//textarea[@name='']").send_keys("Welcome to learn Python")
        driver.find_element_by_link_text(u"发布").click()

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)


if __name__ == "__main__":
    print "11111"
    unittest.main()