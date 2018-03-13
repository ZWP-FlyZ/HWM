# -*- coding: utf-8 -*-
'''
Created on 2018年3月13日

@author: zwp
'''
from main.packing_processer import  pack_all;


if __name__ == '__main__':
    
    predict_result = {
        'flavor1':[1,2,3,4,5,6,7],
        'flavor2':[1,0,1,0,0,0,1],
        'flavor3':[1,0,1,3,2,2,2],
        'flavor4':[1,2,0,0,1,0,3],
        'flavor5':[1,0,0,1,0,0,1]
        }
    pack_all();
    pass