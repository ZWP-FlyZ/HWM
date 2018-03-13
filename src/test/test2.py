# -*- coding: utf-8 -*-
'''
Created on 2018年3月13日

@author: zwp
'''
import copy;

def predict_model1(his_data,# 某种类型的虚拟机的历史数据
                   date_range_size):# 需要预测的长度

    '''
    预测方案一,使用MV 模型预测，
    历史长度为n个粒度时间，权重设定暂定，
    '''
    n =  7; # 历史长度
    # 权重，从最近到最久，长度为n
    ws = [0.45,0.25, 
          0.15,0.08,
          0.04,0.02,
          0.01]; 
    chis_data = copy.deepcopy(his_data);
    for rept in range(date_range_size):
        cal_len = len(chis_data);
        tmpn=0;
        predict=0.0;
        for i in range(cal_len-1,-1,-1):
            predict+= chis_data[i] * ws[tmpn];
            tmpn+=1;
            if tmpn==n:break;
        chis_data.append(int(predict));
        
    return chis_data[len(his_data):];


if __name__ == '__main__':
    his_data=[1,2,3,4,
              5,6,7,8]
    print predict_model1(his_data,3);


