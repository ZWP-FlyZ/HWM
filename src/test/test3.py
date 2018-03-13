# -*- coding: utf-8 -*-
'''
Created on 2018年3月13日

@author: zwp
'''
import math;

VM_TYPE_DIRT =['flavor1','flavor2','flavor3','flavor4','flavor5',
               'flavor6','flavor7','flavor8','flavor9','flavor10',
               'flavor11','flavor12','flavor13','flavor14','flavor15'];


if __name__ == '__main__':
    print VM_TYPE_DIRT.index('flavor10');
    print VM_TYPE_DIRT.index('flavor15');
    
    n =  7; # 历史长度
    # 权重，从最近到最久，长度为n
    ws = [];
    ws_sum = 0.0;
    for i in range(n):
        tmp = 1.0/(1.0+i);
        ws_sum += tmp;
        ws.append(tmp);
    for i in range(n):
        ws[i] = ws[i]/ws_sum;
    print ws;
    pass