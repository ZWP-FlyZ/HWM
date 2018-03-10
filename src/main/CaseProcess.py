# -*- coding: utf-8 -*-
'''
Created on 2018年3月10日

@author: zwp
'''
from datetime import timedelta;
from datetime import datetime;

import ParamInfo; 


class CaseInfo(object):
    '''
    Case的一些信息
    训练用的各个历史信息
    '''
    CPU=0;# cpu数
    MEM=0;# 内存存储量 单位Gb
    HDD=0;# 硬盘存储量 单位Gb
    
    opt_target='';# 优化目标，值为CPU和MEM
    
    vm_types_size=0;# 虚拟机类型数
    vm_types=[];# 虚拟机类型
    
    time_grain = -1; # 预测时间粒度
    date_range_size=0;# 需要预测的时间量
    data_range=[];#预测开始时间与结束时间，左闭右开
    
    # 训练数据中虚拟机、日期二维映射表 [虚拟机类型,日期]
    his_data={};
                

    def __init__(self, origin_case_info,origin_train_data,predict_time_grain=ParamInfo.TIME_GRAIN_DAY):
        '''
        origin_data  predictor中的input_lines数组
        origin_train_data predictor中的ecs_lines数组
        初始化CaseInfo中的属性
        '''
        self.time_grain = predict_time_grain;
        self.set_case_info(origin_case_info,predict_time_grain);
        self.set_his_data(origin_train_data, predict_time_grain);
        pass;
    
    def set_case_info(self,origin_case_info,predict_time_grain):
        '''
        更改 案例属性信息
        info[0]=CPU MEM HDD
        info[2]=vm_type_size
        info[3:(3+vm_type_size)]=vm_types
        info[4+vm_type_size]=opt_target;
        info[6+vm_type_size]=start_time;
        info[7+vm_type_size]=start_time;
        '''
        if (origin_case_info is None) or \
            len(origin_case_info) < 2:
            raise ValueError('Error origin_case_info=',origin_case_info);
        
        # 处理 CPU MEM HDD
        tmp = origin_case_info[0].replace('\r\n','');
        tmps = tmp.split(' ');
        self.CPU=int(tmps[0]);
        self.MEM=int(tmps[1]);
        self.HDD=int(tmps[2]);
        
        # 处理虚拟机类型
        tsize = int(origin_case_info[2].replace('\r\n',''));
        self.vm_types_size = tsize;
        self.vm_types=[];
        for i in range(self.vm_types_size):
            _type = origin_case_info[3+i].replace('\r\n','');
            _typename = _type.split(' ')[0];
            self.vm_types.append(_typename);
        # 处理优化目标    
        self.opt_target = origin_case_info[4+tsize].replace('\r\n','');
        # 处理时间
        _st = origin_case_info[6+tsize].replace('\n','');# bug here ?
        _et = origin_case_info[7+tsize].replace('\n','');# bug here ?
        print _st,_et;
        st = datetime.strptime(_st,"%Y-%m-%d %H:%M:%S");
        et = datetime.strptime(_et,'%Y-%m-%d %H:%M:%S');
        td = et-st;
        if predict_time_grain == ParamInfo.TIME_GRAIN_DAY:
            self.date_range_size = td.days;
        elif predict_time_grain == ParamInfo.TIME_GRAIN_HOUR:
            self.date_range_size = td.days*24 + td.seconds/ 3600 ;
        else:
            self.date_range_size = td.days;
        self.data_range=[_st,_et];
    
    def set_his_data(self,origin_train_data,predict_time_grain):
        if (origin_train_data is None) or \
            len(origin_train_data) ==0 :
            raise ValueError('Error origin_train_data=',origin_train_data);
        hisdata = {};
        
        for line in origin_train_data:
            line = line.replace('\r\n','');
            _,vmtype,time=line.split('\t');
            if not isContainKey(hisdata, vmtype):
                hisdata[vmtype]={};
            gt = get_grain_time(time,predict_time_grain);
            point = hisdata[vmtype];
            if not isContainKey(point,gt):
                point[gt]=0;
            cot = point[gt]+1;
            point[gt]=cot;
        self.his_data = hisdata;

    def add_his_data(self,origin_train_data):
        '''
        在原时间粒度下，添加历史数据信息
        '''
        if (origin_train_data is None) or \
            len(origin_train_data) ==0 :
            raise ValueError('Error origin_train_data=',origin_train_data);
        hisdata=self.his_data;
        for line in origin_train_data:
            line = line.replace('\r\n','');
            _,vmtype,time=line.split('\t');
            if not isContainKey(hisdata, vmtype):
                hisdata[vmtype]={};
            gt = get_grain_time(time,self.time_grain);
            point = hisdata[vmtype];
            if not isContainKey(point,gt):
                point[gt]=0;
            cot = point[gt]+1;
            point[gt]=cot;
        self.his_data = hisdata;
     
    def get_his_data_by_vmtype(self,vmtype):
        '''
        返回一个从第一个数据时间到预测开始前的数据统计列表
        [[时间标签],[值]]
        '''
        tdict = self.his_data[vmtype];
        tkeys = tdict.keys();
        tkeys.sort();
        result = {'time':[], # 时间标签
                  'value':[]};# 统计值
        hrs = 1;
        if self.time_grain == ParamInfo.TIME_GRAIN_DAY:
            hrs = 24;
        td = timedelta(hours=hrs);
        st = datetime.strptime(tkeys[0],'%Y-%m-%d %H:%M:%S');
        et = datetime.strptime(self.data_range[0],'%Y-%m-%d %H:%M:%S');

        while st<et:
            timestr = st.strftime('%Y-%m-%d %H:%M:%S');
            result['time'].append(timestr);
            if timestr in tkeys:
                result['value'].append(tdict[timestr]);
            else:
                result['value'].append(0);
            st = st+td;
            
        return result;    
        
        
        
        
        
        pass;          

################### class CaseInfo end #############################


# 获取粒度时间
split_append_tmp=[[13,':00:00'],[10,' 00:00:00']];
def get_grain_time(time_str,time_grain):
    sp_len_tmp = split_append_tmp[time_grain][0];
    sp_str_tmp = split_append_tmp[time_grain][1];
    return time_str[:sp_len_tmp]+sp_str_tmp;

# 检查dict中是否存在key
def isContainKey(dic,key):
    return key in dic.keys();




        
        
        