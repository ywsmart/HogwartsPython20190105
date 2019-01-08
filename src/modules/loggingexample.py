#!/usr/bin/env python
#coding=utf-8

import logging
from logging.handlers import RotatingFileHandler
from logging.handlers import TimedRotatingFileHandler
import morelog

def log_basic():
    # CRITICAL 50; ERROR 40; WARNING 30; INFO 20; DEBUG 10, NOSET 0;
    logging.basicConfig(filename="web.log", level=0,
                        format='%(asctime)s %(name)s %(levelname)s %(module)s:%(lineno)d %(message)s')
    # logging.basicConfig(stream=sys.stdout,level=int(sys_cfg.get('sysparm','log_level')),format='%(asctime)s %(name)s %(levelname)s %(module)s:%(lineno)d %(message)s')

    logging.getLogger("paramiko").setLevel(logging.WARNING)
    logging.getLogger("selenium").setLevel(logging.WARNING)

    logging.debug("this is debug log")
    logging.info("test info log")



def log_rotate():
    format='%(asctime)s %(name)s %(levelname)s %(module)s:%(lineno)d %(message)s'
    logging.basicConfig(level=20,format='%(asctime)s %(name)s %(levelname)s %(module)s:%(lineno)d %(message)s')

    #定义RotatingFileHandler，日志文件大小超过10M时进行旋转，最大5个备份日志文件。
    rotateHandler = RotatingFileHandler('you.log', maxBytes=1024*0.01, backupCount=5)
    #rotateHandler.setLevel(logging.DEBUG)
    rotateHandler.setFormatter(logging.Formatter(format))
    logging.getLogger("").addHandler(rotateHandler)
    logging.getLogger().propagate = False

    logging.info("my log"*500)


if __name__=="__main__":
    log_basic()
    #log_rotate()