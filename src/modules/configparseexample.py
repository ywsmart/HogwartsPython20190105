#!/usr/bin/env python
#coding=utf-8

import ConfigParser

def get_cfg(in_file):
    config =ConfigParser.ConfigParser()
    config.read(in_file)
    return config

cfg = get_cfg("test.cfg")
print cfg.get("mail_server","smtp_host")
print cfg.get("tomcat_server","ip_address")
