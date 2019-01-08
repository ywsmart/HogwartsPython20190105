#!/usr/bin/env python
#coding=utf-8

import csv
import pprint

def display_data(city_file):
    csvfile = open(city_file, 'r')
    reader = csv.DictReader(csvfile)

    while 1:
        display = input('\nWould you like to view individual trip data?'
                        'Type \'yes\' or \'no\'.\n')
        if display.strip().lower() =="yes":
            for row in range(1,6):
                pprint.pprint(reader.next(),indent=2)
        elif display.strip().lower() =="no":
            csvfile.close()
            break
        else:
            print("the input is wrong, please input yes or no")
    csvfile.close()

display_data("chicago.csv")
