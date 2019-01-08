#!/usr/bin/env python
#coding=utf-8

# 画累和图
import pandas  as pd
import numpy as np
import matplotlib.pyplot  as plt

def pic1():
    ts = pd.Series(np.random.randn(1000), index=pd.date_range('1/1/2000', periods=1000))
    #ts = ts.cumsum()
    print(ts.head(10))
    ts.plot()
    plt.show()

def pic2():
    ts = pd.Series(np.random.randn(1000), index=pd.date_range('1/1/2000', periods=1000))
    df = pd.DataFrame(np.random.randn(1000, 4), index=ts.index, columns=list('ABCD'))
    df = df.cumsum()
    df.plot()
    plt.show()

def pic3():
    # 画柱状图
    df2 = pd.DataFrame(np.random.rand(10, 4), columns=['a', 'b', 'c', 'd'])
    print(df2.head(10))
    df2.plot(kind='bar')  # 分开并列线束
    df2.plot(kind='bar', stacked=True)  # 四个在同一个里面显示 百分比的形式
    df2.plot(kind='barh', stacked=True)  # 纵向显示
    plt.show()

def pic4():
    df4 = pd.DataFrame({'a': np.random.randn(1000) + 1, 'b': np.random.randn(1000), 'c': np.random.randn(1000) - 1},
                       columns=list('abc'))
    df4.plot(kind='hist', alpha=0.5)
    df4.plot(kind='hist', stacked=True, bins=20)
    df4['a'].plot(kind='hist', orientation='horizontal', cumulative=True)  # cumulative是按顺序排序，加上这个
    plt.show()

def pic5():
    # Area Plot
    df = pd.DataFrame(np.random.rand(10, 4), columns=['a', 'b', 'c', 'd'])
    df.plot(kind='area')
    df.plot(kind='area', stacked=False)
    plt.show()

def pic6():
    # 散点图
    df = pd.DataFrame(np.random.rand(50, 4), columns=['a', 'b', 'c', 'd'])
    print(df.head(20))
    df.plot(kind='scatter', x='a', y='b')
    df.plot(kind='scatter', x='a', y='b', color='DarkBlue', label='Group 1')
    plt.show()

def pic7():
    # 饼图
    df = pd.DataFrame(3 * np.random.rand(4, 2), index=['a', 'b', 'c', 'd'], columns=['x', 'y'])
    print(df.head(10))
    df.plot(kind='pie', subplots=True, figsize=(8, 4))
    df.plot(kind='pie', subplots=True, autopct='%.2f', figsize=(8, 4))  # 显示百分比
    plt.show()

def pic8():
    # 画矩阵散点图
    df = pd.DataFrame(np.random.randn(1000, 4), columns=['a', 'b', 'c', 'd'])
    pd.scatter_matrix(df, alpha=0.2, figsize=(6, 6), diagonal='kde')
    plt.show()

def pic9():
    # 饼图
    df = pd.DataFrame(3 * np.random.rand(4, 1), index=['a', 'b', 'c', 'd'], columns=['x'])
    print(df.head(10))
    df.plot(kind='pie', subplots=True, figsize=(8, 4))
    df.plot(kind='pie', subplots=True, autopct='%.2f', figsize=(8, 4))  # 显示百分比
    plt.show()

if __name__=="__main__":
    pic3()
