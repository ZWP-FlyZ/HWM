# -*- coding: utf-8 -*-
'''
Created on 2018年3月10日

@author: zwp
'''

import platform;

# 所有虚拟机的参数
# [CPU,MEM, W(M/C) ] [U数，M数，存储比核的权重]
VM_PARAM = {
    'flavor1':[1,1,1.0],
    'flavor2':[1,2,2.0],
    'flavor3':[1,4,4.0],
    
    'flavor4':[2,2,1.0],
    'flavor5':[2,4,2.0],
    'flavor6':[2,8,4.0],
    
    'flavor7':[4,4,1.0],
    'flavor8':[4,8,2.0],
    'flavor9':[4,16,4.0],
    
    'flavor10':[8,8,1.0],
    'flavor11':[8,16,2.0],
    'flavor12':[8,32,4.0],
    
    'flavor13':[16,16,1.0],
    'flavor14':[16,32,2.0],
    'flavor15':[16,64,4.0]
    }
VM_TYPE_DIRT =['flavor1','flavor2','flavor3','flavor4','flavor5',
               'flavor6','flavor7','flavor8','flavor9','flavor10'
               'flavor11','flavor12','flavor13','flavor14','flavor15'];
# 预测时间粒度
# 
TIME_GRAIN_HOUR = 0;
TIME_GRAIN_DAY = 1;
TIME_GRAIN_MORE_DAY = 2; 


# 系统检查
sysstr = platform.system();
end_str = '';
if(sysstr =="Windows"):
    end_str = '\n';
elif(sysstr == "Linux"):
    end_str = '\r\n';

            





