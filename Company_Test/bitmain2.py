# -*- coding: utf-8 -*-
"""
Created on Sat Oct 20 20:19:48 2018

@author: Ray
"""

def swap_odd_and_even(mylist):
    length = len(mylist)
    for i in range(length):
        if (mylist[i]%2 == 0):
            mylist.append(mylist[i])
            mylist.pop(i)

if __name__ == '__main__':
    mylist = [3,8,9,6,5,4,7,1,2]
    mylist = [x for x in range(50)]
    swap_odd_and_even(mylist)
    print(mylist)