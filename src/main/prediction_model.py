# -*- coding: utf-8 -*-
'''
Created on 2018年3月10日

@author: zwp12
'''

'''
    预测模型，输入CaseInfo对象，
    输出在预测期内各个虚拟机类型的请求数量
    
'''

import copy;

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
        chis_data.append(int(predict));
        result.append(int(predict));
    return result;



def predict_all(caseInfo):
    '''
    输入为CaseInfo对象，
    返回一个结果对象，结构为{vm_type:[v1,v2,v3....]};
    数组长度为caseInfo,中date_range_size,代表各个时间粒度内，
    该虚拟机被请求数,
    注意：当前预测模型设置只适合各个虚拟机类型独立预测
    '''
    result = {};
    vm_types = caseInfo.vm_types;
    for vmtype in vm_types:
        result[vmtype] = predict_one(vmtype,caseInfo,predict_model1);
    return result;   


def predict_one(vm_type,# 虚拟机类型
                caseInfo,# 案例信息对象
                prodict_function=None# 时间序列预测
                ):
    return prodict_function(caseInfo.get_his_data_by_vmtype(vm_type),
                            caseInfo.date_range_size);
    '''
    训练并预测一种虚拟机的类型，返回为
    一个[v1,v2,v3....]预测结果数组
    '''
    
    #  test here
    # return [1,2,3,4];







