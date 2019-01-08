#!/usr/bin/env python
#coding=utf-8

import pandas as pd
import numpy as np
s = pd.Series(np.random.randn(5), index=['a', 'b', 'c', 'd', 'e'])

pd.Series([1,3,5,np.nan,6,8])