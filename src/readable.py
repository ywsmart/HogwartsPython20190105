#!/usr/bin/env python
#coding=utf-8

def output_keyword(in_file,keyword):
    file = open(in_file,"r")
    for line in file.readlines():
        if keyword in line:
            print line.strip()
    file.close()

print "Hello World"

if __name__ == '__main__':
    output_keyword("readable.csv","China")

