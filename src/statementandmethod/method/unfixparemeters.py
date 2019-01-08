#!/usr/bin/env python
#coding=utf-8


def student(profile,*mytuple):
    out_put=""

    for parameter in mytuple:
        if not out_put:
            out_put = out_put+parameter
        else:
            out_put = out_put +","+ parameter
    return profile+";  "+out_put

print student(u"学生",u"大鹏",u"男性",u"7岁")


def student_tuple(profile,mytuple):
    out_put=""

    for parameter in mytuple:
        if not out_put:
            out_put = out_put+parameter
        else:
            out_put = out_put +","+ parameter
    return profile+";  "+out_put

print student_tuple(u"学生",(u"大鹏",u"男性",u"7岁"))
