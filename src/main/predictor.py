# -*- coding: utf-8 -*-

import CaseProcess;
import packing_processer;
import prediction_model;


def predict_vm(ecs_lines, input_lines):
    # Do your work from here#
    result = []
    if ecs_lines is None:
        print 'ecs information is none'
        return result
    if input_lines is None:
        print 'input file information is none'
        return result
  
    caseInfo = CaseProcess.CaseInfo(input_lines,ecs_lines);
    
    predict_result = prediction_model.predict_all(caseInfo);
    vm_size,vm,pm_size,pm = packing_processer.pack_all(caseInfo, predict_result);
    
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
        if len(pmone.keys())==0:
            continue;
        for index in pmone.keys():
            item = pmone[index];
            tmp += ' '+index+' '+str(item);
        tmp+=end_str;
        result.append(tmp);
    return result;
    




