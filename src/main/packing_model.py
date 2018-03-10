# -*- coding: utf-8 -*-
'''
Created on 2018年3月10日

@author: zwp12
'''

'''
    装配模型，输入为预测模型输出的预测对象，
    在转配模型中可维护一个历史物理机集群状态对象，
    可为另一种转配理解。
'''

import ParamInfo;

class MachineGroup():
    '''
    静态集群状态类
    '''
    
    #物理机操作指针
    ptr = 0;
    
    
    # 集群中物理机参数
    machine_info = {'CPU':0,# u数
                    'MEM':0,# m数
                    'HDD':0}# h数
    
    # 物理机计数
    pm_size = 0;
    # 各个物理机状态，存储值为
    # re_cpu:剩余u数，re_mem:剩余m数，vm_size:当前物理机中虚拟机数
    # [pm_id->{re_cpu:cot,re_mem:cot,vm_size:cot},
    #  pm_id2->{re_cpu:cot,re_mem:cot,vm_size:cot...]
    PM_status=[];
    
    # 当前集群中虚拟机计数
    vm_size = 0;
    # 虚拟机存储状态，对应的存储为
    # {vm_type:cot,vm_type2:cot...}
    VM = {};
    
    # 物理机存储状态，对应存储值
    # [pm_id->{vm_type:cot,vm_type2:cot....},
    #  pm_id2->{vm_type:cot,vm_type2:cot...}...]
    PM = [];
    
    
    def __init__(self,caseInfo):
        '''
        初始化集群，创建一个物理机，并初始化相关参数
        '''
        
        pass;








