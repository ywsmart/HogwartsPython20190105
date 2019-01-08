#!/usr/bin/env python
#coding=utf-8
import subprocess
print subprocess.check_output(["adb", "shell", "top -n 1 | findstr com.android.browser"])
