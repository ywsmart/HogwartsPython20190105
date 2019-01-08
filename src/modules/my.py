#!/usr/bin/env python
#coding=utf-8

import time
from datetime import datetime
import sys
print
reload(sys)
sys.setdefaultencoding('UTF-8')
print sys.getfilesystemencoding()


print time.strftime("%Z").decode(sys.getfilesystemencoding()).encode('utf-8')
print "中国".encode('utf-8').decode('utf-8')