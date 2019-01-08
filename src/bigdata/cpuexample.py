#!/usr/bin/env python
#coding=utf-8

import pandas as pd
import matplotlib.pyplot as plt

def out_cpu_csv(in_file):
    csv_file = open("cpu.csv","w")
    csv_file.write("time,user,system,usage"+"\n")
    with open(in_file,"r") as cpu_content:
        content_lines = cpu_content.readlines()
        monitor_time=''
        user, system, usage="", "",""
        for line in content_lines:
            if "MonitorTime" in line:
                monitor_time = line.strip().split()[1]
            if "Average" in line:
                user,system, usage = line.strip().split()[2],line.strip().split()[4],line.strip().split()[7]
            if monitor_time and user and system and usage:
                csv_file.write(monitor_time+","+user+","+system+","+str(100-float(usage))+"\n")
                csv_file.flush()
                monitor_time = ''
                user, system, usage = "", "", ""

def remove_month(data_frame):
    return data_frame["time"].split("-")[1]


def generate_pic(csv_file):
    cpu_df = pd.read_csv(csv_file, skip_blank_lines=True, encoding="utf8", header=0,index_col=0)

    print(cpu_df.head(20))
    plt.figure()
    # %matplotlib inline
    cpu_df.plot(sharex=True, sharey=True,title=u"CPU Trend")
    #cpu_df.plot()
    usge_sum = cpu_df["usage"].sum(skipna=True)
    print ("avg:", usge_sum/len(cpu_df["usage"].values))
    plt.show()

    cpu_df.reset_index(inplace=True)
    print(type(cpu_df.head(20)))
    cpu_df["Hours"] = cpu_df.apply(remove_month, axis=1)
    cpu_df.drop("time", axis=1, inplace=True)
    cpu_df.set_index("Hours",inplace=True)
    # %matplotlib inline
    cpu_df.plot()
    plt.show()
    # %matplotlib inline
    cpu_df.plot(rot=-30)


    ax = cpu_df.plot(rot=30)
    ax.set_ylabel("CPU Percentage")

    ax = cpu_df.plot(figsize=(80, 20), rot=30)
    ax.set_ylabel("CPU Percentage")

    print (cpu_df.head(100).plot(rot=-30))
    plt.show()


if __name__=="__main__":
    generate_pic("cpu.csv")
    #out_cpu_csv("cpu")



