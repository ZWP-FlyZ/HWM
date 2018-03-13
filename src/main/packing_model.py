# -*- coding: utf-8 -*-
'''
Created on 2018年3月12日

@author: zwp12
'''

def pack_model1(vmPicker,machineGroup,opt_target='CPU'):
    '''
    具体装配方案一,简单的装配方法,
    当优化目标为CPU时，优先装载M/U权重小的并且CPU多的虚拟机，
    当优化目标为MEM时，优先装载M/U权重大的并且CPU少的虚拟机，
    若一个物理机中无法装载着，开新的物理机，依次遍历物理机放置法。
    vmPicker:
    machineGroup:
    opt_target:优化目标[CPU,MEM],默认CPU优化
    '''
    # 获得放置顺序
    vm_orders = [[], # vm_type
                 []] # cot
    weightes = [1,2,4];
    start=0;end=3;step=1;order=0;
    if opt_target == 'MEM':
        start=2;end=-1;step=-1;order=0;
    for wi in range(start,end,step):
        tmp = vmPicker.get_vm_by_mu_weight(weightes[wi],order);
        if tmp != None:
            vm_orders[0].extend(tmp[0]);
            vm_orders[1].extend(tmp[1]);

    vm_type_size = len(vm_orders[0]);
    if vm_type_size ==0:return ;# 无装配项，结束
    for vm_index in range(vm_type_size):
        vm_type = vm_orders[0][vm_index];
        vm_cot = vm_orders[1][vm_index];
        pm_size = machineGroup.pm_size;
        for rept in range(vm_cot):
            is_In = False;
            for pm_id in range(pm_size):
                re_items = machineGroup.put_vm(pm_id,vm_type);
                if re_items != None:
                    is_In=True;
                    break;
            if not is_In : # 在现有的物理机中无法安排该虚拟机
                pm_size = machineGroup.new_physic_machine();
                re_items = machineGroup.put_vm(pm_size-1,vm_type);
                if re_items == None:
                    raise ValueError('ENDLESS LOOP ! ');
    
                    
############################## end model1 ###############################


