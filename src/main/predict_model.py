# -*- coding: utf-8 -*-
'''
Created on 2018年3月13日

@author: zwp
'''

import copy;
import math;


def predict_model1(his_data,# 某种类型的虚拟机的历史数据
                   date_range_size):# 需要预测的长度

    '''
    预测方案一,使用MV 模型预测，
    历史长度为n个粒度时间，权重设定暂定，
    his_data:['time':[时间标签],'value':[值]]
    '''
    n =  7; # 历史长度
    # 权重，从最近到最久，长度为n
    ws = [0.45,0.25, 
          0.15,0.08,
          0.04,0.02,
          0.01]; 
    chis_data = copy.deepcopy(his_data['value']);
    result = [];
    for rept in range(date_range_size):
        cal_len = len(chis_data);
        tmpn=0;
        predict=0.0;
        for i in range(cal_len-1,-1,-1):
            predict+= chis_data[i] * ws[tmpn];
            tmpn+=1;
            if tmpn==n:break;
        predict = int(math.floor(predict));
        chis_data.append(predict);
        result.append(predict);
    return result;


def predict_model2(his_data,# 某种类型的虚拟机的历史数据
                   date_range_size):# 需要预测的长度

    '''
    预测方案一,使用SMV 模型预测，
    历史长度为n个粒度时间，权重设定暂定，
    his_data:['time':[时间标签],'value':[值]]
    '''
    n =  7; # 历史长度
    # 权重，从最近到最久，长度为n
 
    chis_data = copy.deepcopy(his_data['value']);
    result = [];
    for rept in range(date_range_size):
        cal_len = len(chis_data);
        tmpn=0;
        predict=0.0;
        for i in range(cal_len-1,-1,-1):
            predict+= chis_data[i];
            tmpn+=1;
            if tmpn==n:break;
        
        predict = int(math.ceil(predict*1.0/tmpn));
        chis_data.append(predict);
        result.append(predict);
    return result;

