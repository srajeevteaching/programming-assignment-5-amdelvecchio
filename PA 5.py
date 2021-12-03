# Programmers: Anthony DelVecchio
# Course: CS 151, Dr. Rajeev
# Programming Assignment: 5

import os
import tempfile

import numpy as np


def read_file(file):
    data_list=[]
    for line in file:
        data_list.append(line.split(","))
    file.close()
    return data_list
def fixlast(l):
    for x in l:
        x[-1] = x[-1].strip()
    return l


def main():
    path = os.path.join(tempfile.gettempdir(), '2016_09.csv')
    path2 = os.path.join(tempfile.gettempdir(), '2016_10.csv')
    print(path2)
    f = open(path, 'r')
    f2 = open(path2, 'r')
    list_sept = read_file(f)
    list_oct = read_file(f2)
    list_oct = fixlast(list_oct)
    list_sept = fixlast(list_sept)
    print(list_sept)
    print(list_oct)


main()
