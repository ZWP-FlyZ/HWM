

import CaseProcess;

def predict_vm(ecs_lines, input_lines):
    # Do your work from here#
    result = []
    if ecs_lines is None:
        print 'ecs information is none'
        return result
    if input_lines is None:
        print 'input file information is none'
        return result

    for item in ecs_lines:
        item=item.replace('\r\n','');
        values = item.split("\t")
        print(values);
        uuid = values[0]
        flavorName = values[1]
        createTime = values[2]
        
    case = CaseProcess.CaseInfo(input_lines,ecs_lines,1);
    
    print case;
    return result
