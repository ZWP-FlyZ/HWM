# -*- coding: utf-8 -*-
'''
Created on 2018年3月10日

@author: zwp12
'''
import math;

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

################## end class MachineGroup ####################


class VmPicker():
    '''
    输入预测模型的预测结果，
    并维护一个权重与核心数级别的二维映射表，
    调用任何get_xxx 方法会时Picker中的虚拟机数减少，
    直到全部虚拟机被取完。
    二维表中原值为-1,未被预测虚拟机，
    大于等于0表示已被预测的虚拟机数量
    '''
    
    # 预测输入的原始数据
    origin_data = None;
    
    # 虚拟机总数，非零虚拟机总数
    vm_size = 0;
    
    # 预测虚拟机的在M/U权重与核心数级别
    # 上展开 shape=[3,5]
    #   CPU=1,2,4,8,16
    VM = [[-1,-1,-1,-1,-1], # weight_1.0
          [-1,-1,-1,-1,-1], # weight_2.0
          [-1,-1,-1,-1,-1]  # weight_4.0
        ];
    
    # 虚拟机类型名数组
    vm_types = ParamInfo.VM_TYPE_DIRT;
    
    def __init__(self,predict_result):
        self.origin_data = predict_result;
        self.init_picker(predict_result);
        pass;
    
    def init_picker(self,predict_result):
        types = predict_result.keys();
        for vmtype in types:
            vsum = 0;
            pre  =  predict_result[vmtype];
            for i in range(len(pre)):
                vsum+=pre[i];
            windex,cindex = self.type2index(vmtype);
            self.VM[windex][cindex] = vsum;
        pass;
    
    
    def type2index(self,vm_type):
        tindex = self.vm_types.index(vm_type);
        windex = tindex % 3;
        cindex = int(tindex / 3);
        return windex,cindex;

    def index2type(self,windex,cindex):
        if windex < 0 or cindex < 0:
            raise ValueError('Error ',(windex,cindex));
        return self.vm_types[cindex*3 + windex];
    
    def get_vm_by_index(self,windex,cindex):
        '''
        windex M/U权重的下标 cindex CPU数下标，
        若原先并没有预测则返回None,拿取失败
        若原先有预测但当前数量为0,返回-1,拿取失败，
        正常情况 返回 该虚拟机类型剩余量
        '''
        re_vm = self.VM[windex][cindex];
        if re_vm==-1:
            return None;
        elif re_vm == 0:
            return -1;
        else:
            re_vm-=1;
        self.VM[windex][cindex] = re_vm;
        return re_vm;
        pass;


    def get_vm_by_wc(self,weight,cpu):
        '''
        通过虚拟机M/U权重和CPU数获取，
        若原先并没有预测则返回None,拿取失败
        若原先有预测但当前数量为0,返回-1,拿取失败，
        正常情况 返回 该虚拟机类型剩余量
        '''
        windex = int(math.log(weight,2));
        cindex = int(math.log(cpu,2));
        return self.get_vm_by_index(windex,cindex);
        pass;
    
    def get_vm_by_type(self,vm_type):
        '''
        通过虚拟机类型名获取，
        若原先并没有预测则返回None,拿取失败
        若原先有预测但当前数量为0,返回-1,拿取失败，
        正常情况 返回 该虚拟机类型剩余量
        '''
        windex,cindex = self.type2index(vm_type);
        return self.get_vm_by_index(windex,cindex);
    
    pass;





