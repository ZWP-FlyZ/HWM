

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
    print(group.PM_status);
    group.new_physic_machine();
    group.new_physic_machine();
    group.new_physic_machine();
    group.new_physic_machine();
    print(group.put_vm(2, 'flavor15'));
    print(group.put_vm(2, 'flavor15'));
    print(group.put_vm(2, 'flavor15'));
    print(group.put_vm(2, 'flavor15'));    
    print(group.put_vm(2, 'flavor15'));
    
    
    
    predict_result = {'flavor2':[1,2,3,4],
                      'flavor3':[0,0,0,0],
                      'flavor7':[1,0,0,4]}
    
    picker = packing_model.VmPicker(predict_result);
    
    print(picker.get_vm_by_type('flavor3'));
    print(picker.get_vm_by_type('flavor2'));
    print(picker.get_vm_by_type('flavor1'));
    
    print(picker);
    
    
    return result
