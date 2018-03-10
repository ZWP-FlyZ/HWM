

import CaseProcess;
import ParamInfo;

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
    return result
