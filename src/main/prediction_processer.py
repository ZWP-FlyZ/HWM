# -*- coding: utf-8 -*-
'''
Created on 2018年3月10日

@author: zwp12
'''

'''
    预测模型，输入CaseInfo对象，
    输出在预测期内各个虚拟机类型的请求数量
    
'''

import predict_model;

predict_func = predict_model.used_func;

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
        result[vmtype] = predict_one(vmtype,caseInfo,predict_func);
    return result;   


def predict_one(vm_type,# 虚拟机类型
                caseInfo,# 案例信息对象
                prodict_function=None# 时间序列预测
                ):
    return prodict_function(caseInfo.get_his_data_by_vmtype_avage_v2(vm_type,-1),
                            caseInfo.date_range_size);
    '''
    训练并预测一种虚拟机的类型，返回为
    一个[v1,v2,v3....]预测结果数组
    '''
    
    #  test here
    # return [1,2,3,4];







