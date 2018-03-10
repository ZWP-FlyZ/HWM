# -*- coding: utf-8 -*-
'''
Created on 2018年3月10日

@author: zwp12
'''

'''
    预测模型，输入CaseInfo对象，
    输出在预测期内各个虚拟机类型的请求数量
    
'''

import ParamInfo;

def predict_all(caseInfo):
    '''
    输入为CaseInfo对象，
    返回一个结果对象，结构为{vm_type:[v1,v2,v3....]};
    数组长度为caseInfo,中date_range_size,代表各个时间粒度内，
    该虚拟机被请求数
    '''
    pass;

def predict_one(vm_type,# 虚拟机类型
                caseInfo,# 案例信息对象
                prodict_function=None# 时间序列预测
                ):
    '''
    训练并预测一种虚拟机的类型，返回为
    一个[v1,v2,v3....]预测结果数组
    '''
    
    pass;

def predict_model1():
    '''
    预测方案一
    '''
    pass;





