#!/usr/bin/env python
#coding=utf-8



import subprocess

#print subprocess.check_output(r"C:\Windows\System32\notepad.exe", shell=True)
#print subprocess.check_output("path", shell=True)

print subprocess.check_call("path", shell=True)
#print subprocess.call("ipconfig -all", shell=True)