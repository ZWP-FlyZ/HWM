# -*- coding: utf-8 -*-

import CaseProcess;
import ParamInfo;
import packing_model;


def predict_vm(ecs_lines, input_lines):
    # Do your work from here#
    result = []
    if ecs_lines is None:
        print 'ecs information is none'
        return result
    if input_lines is None:
        print 'input file information is none'
        return result

        
    case = CaseProcess.CaseInfo(input_lines,ecs_lines);
    
    keys = case.his_data['flavor2'].keys();
    print(keys.sort());
    print(keys);
    print(case.get_his_data_by_vmtype('flavor2'));
    
    group = packing_model.MachineGroup(case);
    print(group.put_vm(0, 'flavor13'));
    print(group.put_vm(0, 'flavor13'));
    print(group.put_vm(0, 'flavor13'));
    print(group.put_vm(0, 'flavor13'));
#     print(group.PM_status);
#     group.new_physic_machine();
#     group.new_physic_machine();
#     group.new_physic_machine();
#     group.new_physic_machine();
#     print(group.put_vm(2, 'flavor15'));
#     print(group.put_vm(2, 'flavor15'));
#     print(group.put_vm(2, 'flavor15'));
#     print(group.put_vm(2, 'flavor15'));    
#     print(group.put_vm(2, 'flavor15'));
    
    
    
    predict_result = {'flavor2':[1,2,3,4],
                      'flavor3':[0,0,0,0],
                      'flavor7':[1,0,0,4]}
    
    picker = packing_model.VmPicker(predict_result);
    
    print(picker.get_vm_by_type('flavor3'));
    print(picker.get_vm_by_type('flavor2'));
    print(picker.get_vm_by_type('flavor1'));
    
    print(picker);
    
    vm_size,vm = picker.to_origin_desc();
    
    pm_size,pm = group.to_description();
    
    result = result_to_list(vm_size, vm, pm_size, pm);
    print(result);
    return result



def result_to_list(vm_size,vm,pm_size,pm):
    '''
    由预测和分配生成结果
    vm：{vm_type:cot...}
    pm[{vm_type:cot,vm_type2:cot2...}...]
    '''
    end_str='';
    result=[];
    result.append(str(vm_size)+end_str);
    for index in vm.keys():
        item = vm[index];
        tmp = index +' '+str(item)+end_str;
        result.append(tmp);
        
    result.append(end_str);
    
    result.append(str(pm_size)+end_str);
    for pm_id in range(len(pm)):
        tmp = str(pm_id);
        pmone = pm[pm_id];
        for index in pmone.keys():
            item = pmone[index];
            tmp += ' '+index+' '+str(item);
        tmp+=end_str;
        result.append(tmp);
    return result;
    




