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
        self.machine_info['CPU']= caseInfo.CPU;
        self.machine_info['MEM']= caseInfo.MEM;
        self.machine_info['HDD']= caseInfo.HDD;
        self.new_physic_machine();
        pass;

    def new_physic_machine(self):
        '''
        创建一个新的物理机，
        '''
        self.pm_size+=1;
        npm = {
            're_cpu':self.machine_info['CPU'],
            're_mem':self.machine_info['MEM'],
            'vm_size':0
            };
        self.PM_status.append(npm);
        self.PM.append({});

    def put_vm(self,pm_id,vm_type):
        '''
        放置一个虚拟机，
        pm_id为物理机ID，vm_type为虚拟机类型名
        如果放置成功 返回放置后的物理机(re_cpu,re_mem)，
        因空间不足放置失败返回None
        '''
        if pm_id is None or \
        pm_id<0 or pm_id>=self.pm_size:
            raise ValueError('error pm_id=',pm_id);
        vm_cpu,vm_mem = ParamInfo.VM_PARAM[vm_type][:2];
        pmstatus = self.PM_status[pm_id];
        re_cpu = pmstatus['re_cpu']-vm_cpu;
        re_mem = pmstatus['re_mem']-vm_mem;
        if re_cpu>=0 and  re_mem>=0:
            pmstatus['re_cpu'] = re_cpu;
            pmstatus['re_mem'] = re_mem;
            pmstatus['vm_size'] +=1;
            self.vm_size+=1;
            if vm_type not in self.VM.keys():
                self.VM[vm_type]=0;
            self.VM[vm_type]+=1;
            pm = self.PM[pm_id];
            if vm_type not in pm.keys():
                pm[vm_type]=0;
            pm[vm_type]+=1;
            return (re_cpu,re_mem);
        return None; # 超分返回




