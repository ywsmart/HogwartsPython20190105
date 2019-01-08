#!/usr/bin/env python
# coding=utf-8


from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import unittest, time, re

options = Options()
options.add_argument("--disable-notifications")
driver = webdriver.Chrome(chrome_options=options)
driver.implicitly_wait(30)

driver.get("https://weibo.com/login.php")
driver.find_element_by_id("loginname").click()
driver.find_element_by_id("loginname").clear()
driver.find_element_by_id("loginname").send_keys("tyjfen@sina.com")
driver.find_element_by_name("password").clear()
driver.find_element_by_name("password").send_keys("123456@Fang")
#time.sleep(2)
#driver.switch_to.alert.accept()
driver.find_element_by_id("login_form_savestate").click()
#driver.find_element_by_xpath('//*[@id="pl_login_form"]/div/div[3]/div[6]/a').click()
driver.find_element_by_xpath("//div[@id='pl_login_form']/div/div[3]/div[6]/a").click()
time.sleep(5)
driver.find_element_by_xpath("//textarea[@name='']").clear()
driver.find_element_by_xpath("//textarea[@name='']").send_keys("my test weibo")
driver.find_element_by_link_text(u"发布").click()