#!/usr/bin/env python
#coding=utf-8

import pandas as pd

d = {'name' : pd.Series(["zhangsan", "lisi", "hanmeimei"], index=[1, 2, 3]),
     'sex' : pd.Series(["Mael", "Mael", "Male", "Male"], index=[1, 2, 3, 4])}

df = pd.DataFrame(d)
print(df)