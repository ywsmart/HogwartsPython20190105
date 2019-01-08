#!/usr/bin/env python
#coding=utf-8

import pandas as pd
import matplotlib.pyplot  as plt

def get_month(data_frame):
    return data_frame["Date"].strftime("%Y%m")

def bar_kpi():
    kpi_pd = pd.read_excel("kpi.xlsx",sheet_name="Sheet1")
    kpi_pd["month"] = kpi_pd.apply(get_month, axis=1)
    print(kpi_pd.head(10))

    #print kpi_pd.groupby(['month', 'Service']).count()
    kpi_pd["count_column"]=kpi_pd.groupby(['month', 'Service']).Service.transform('count')
    #print kpi_pd.head(10)

    monthly_df =pd.DataFrame()
    monthly_df["month"]=kpi_pd["month"]
    monthly_df["Service"]=kpi_pd["Service"]
    monthly_df["count_column"]=kpi_pd["count_column"]
    monthly_df.drop_duplicates(inplace=True)
    #montly_df.set_index("month",inplace=True)
    print(monthly_df.head(10))


    products_dic ={}
    print(set(monthly_df["month"].tolist()))
    for month in set(monthly_df["month"].tolist()):
        for product in set(monthly_df["Service"].tolist()):
            release_no = monthly_df[(monthly_df['month'] == month) & (monthly_df['Service'] == product)]["count_column"].tolist()
            #py2 if not products_dic.has_key(product):
            if not (product in products_dic):
                if release_no:
                    products_dic[product] = [release_no[0]]
                else:
                    products_dic[product] = [0]
            else:
                if release_no:
                    products_dic[product].append(release_no[0])
                else:
                    products_dic[product].append(0)

    products_dic["month"] = list(set((monthly_df["month"].tolist())))
    print(products_dic)


    release_kpi = pd.DataFrame(products_dic)
    release_kpi.set_index("month",inplace=True)
    release_kpi.sort_index(axis=0, inplace=True)
    print(release_kpi.head(10))
    release_kpi.plot(kind='bar',rot=30)
    ax = release_kpi.plot(kind='bar', stacked=True,rot=30)
    ax.set_ylabel("Release Number")
    release_kpi.plot(kind='barh', stacked=True,rot=30)
    plt.show()

def pie_kpi():
    bug_kpi = pd.DataFrame({"Name":["Tom","Hanmeimei","Zhuzhu","Jianmei","Jun","Sary","Hu"],
                             "Bug":[160,180,340,670,70,302,90]})
    bug_kpi.set_index("Name",inplace=True)
    bug_kpi.plot(kind='pie', subplots=True, figsize=(8, 4))
    bug_kpi.plot(kind='pie', subplots=True, autopct='%.2f', figsize=(8, 4))
    bug_kpi.plot(kind='pie', subplots=True, autopct='%.2f',legend= False, title="Bug Distribution")
    plt.axes().set_ylabel('')
    plt.show()


duration_kpi = pd.DataFrame({"sessionid":["s1","s2","s3","s4","s5","s6","s7"],
                             "request":[1515677949915,1515677949925,1515677949935,1515677949942,1515677949944,1515677949945,1515677949947],
                             "response": [1515677949918, 1515677949929, 1515677949936, 1515677949947, 1515677949947,
                                    1515677949949, 1515677949957]})


if __name__=="__main__":
    pie_kpi()
    bar_kpi()









