#!/usr/bin/env python
#coding=utf-8

from shutil import make_archive
import os

def targz_dir():
    archive_name = "myimage"
    root_dir = "../image"
    make_archive(archive_name, 'gztar', root_dir)

if __name__=="__main__":
    targz_dir()