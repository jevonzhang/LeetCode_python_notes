# -*- coding: utf-8 -*-
"""
Created on Wed Jan 31 21:31:34 2018

@author: jevon_z
"""


nums =  [2,7,11,15]

target  = 9

dic = {}    #空字典


for index, num in enumerate(nums):
    if num in dic:      #如何进入if语句
        print("dicnum:%i"%dic[num])
#字典会根据dic[num]和dic[target - num]更新dic key值从0开始
        print("indexif:%i"%index)
        print("numif:%i"%num)
    dic[target - num] = index
    print("numelse:%i"%num)
    print("indexelse:%i"%index)
    print("dictgnum:%i"%dic[target - num])
    print('\n')