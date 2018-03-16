# -*- coding: utf-8 -*-
'''
Created on 2018年3月13日

@author: zwp
'''

import copy;
import math;
import random;


def predict_model1(his_data,# 某种类型的虚拟机的历史数据
                   date_range_size):# 需要预测的长度

    '''
    预测方案一,使用MV模型预测，最近n天 
    历史长度为n个粒度时间，权重设定暂定，
    his_data:['time':[时间标签],'value':[值]]
    '''
    n =  7; # 历史长度
    # 权重，从最近到最久，长度为n
    ws = [0.45,0.25, 
          0.15,0.08,
          0.04,0.02,
          0.01]; 
    chis_data = copy.deepcopy(his_data['value']);
    result = [];
    for rept in range(date_range_size):
        cal_len = len(chis_data);
        tmpn=0;
        predict=0.0;
        for i in range(cal_len-1,-1,-1):
            predict+= chis_data[i] * ws[tmpn];
            tmpn+=1;
            if tmpn==n:break;
        predict = int(math.floor(predict));
        chis_data.append(predict);
        result.append(predict);
    return result;


def predict_model2(his_data,# 某种类型的虚拟机的历史数据
                   date_range_size):# 需要预测的长度

    '''
    预测方案二,使用SMV 模型预测， 最近n天
    历史长度为n个粒度时间，权重设定暂定，
    his_data:['time':[时间标签],'value':[值]]
    '''
    n =  7; # 历史长度
    # 权重，从最近到最久，长度为n
 
    chis_data = copy.deepcopy(his_data['value']);
    result = [];
    for rept in range(date_range_size):
        cal_len = len(chis_data);
        tmpn=0;
        predict=0.0;
        for i in range(cal_len-1,-1,-1):
            predict+= chis_data[i];
            tmpn+=1;
            if tmpn==n:break;
        
        predict = int(math.ceil(predict*1.0/tmpn));
        chis_data.append(predict);
        result.append(predict);
    return result;

def predict_model3(his_data,# 某种类型的虚拟机的历史数据
                   date_range_size):# 需要预测的长度

    '''
    预测方案3,使用MV 模型预测，最近n天
    历史长度为n个粒度时间，使用倒数权重，
    his_data:['time':[时间标签],'value':[值]]
    '''
    n =  10; # 历史长度
    # 权重，从最近到最久，长度为n
    ws = [];
    ws_sum = 0.0;
    for i in range(n):
        # tmp = 1.0/(1.0+i);
        tmp = math.exp(-1.0*i);
        ws_sum += tmp;
        ws.append(tmp);
    for i in range(n):
        ws[i] = ws[i]/ws_sum;
    
    chis_data = copy.deepcopy(his_data['value']);
    result = [];
    for rept in range(date_range_size):
        cal_len = len(chis_data);
        tmpn=0;
        predict=0.0;
        for i in range(cal_len-1,-1,-1):
            predict+= chis_data[i] * ws[tmpn];
            tmpn+=1;
            if tmpn==n:break;
        predict = int(math.ceil(predict));
        chis_data.append(predict);
        result.append(predict);
    return result;

def predict_model4(his_data,# 某种类型的虚拟机的历史数据
                   date_range_size):# 需要预测的长度

    '''
    预测方案四,使用SMV 模型预测，添加正态随机噪声  最近n天
    历史长度为n个粒度时间，权重设定暂定，
    his_data:['time':[时间标签],'value':[值]]
    '''
    n =  13; # 历史长度
    sigma = 0.4;
 
    
    chis_data = copy.deepcopy(his_data['value']);
    result = [];
    for rept in range(date_range_size):
        cal_len = len(chis_data);
        tmpn=0;
        predict=0.0;
        for i in range(cal_len-1,-1,-1):
            predict+= chis_data[i];
            tmpn+=1;
            if tmpn==n:break;
        noise = random.gauss(0,sigma);
        predict = int(math.ceil(predict*1.0/tmpn+noise));
        chis_data.append(predict);
        result.append(predict);
    return result;


def front_out(w,b,x):
    suma = 0.0;
    for i in range(len(w)):
        suma += w[i]*x[i];
    return suma+b[0];

def change(w,b,x,py_y,lr):
    for i in range(len(w)):
        w[i] -= py_y*x[i]*lr;
    b[0] -= lr* py_y;

    
def predict_model5(his_data,# 某种类型的虚拟机的历史数据
                   date_range_size):# 需要预测的长度

    '''
    预测方案5,进行一次差分，然后使用MA处理   失败
    历史长度为n个粒度时间，使用倒数权重，
    his_data:['time':[时间标签],'value':[值]]
    '''
    n =  10; # 历史长度
    sigma = 0.1;
    # 权重，从最近到最久，长度为n
    lr = 0.01;
    
    origin_data = his_data['value'];
    chis_data = copy.deepcopy(origin_data);
    
    # 差分,计算平均
    diff = [];
    avag = [];
    for i in range(1,len(chis_data)):
        b = origin_data[i];
        a = origin_data[i-1];
        diff.append(b-a);
        avag.append((a+b)/2.0);
    avag.append(origin_data[-1]);
    
    print 'diff',diff;
    print 'avag',avag;
    result = [];
    
    w = [];
    for i in range(n):
        w.append(random.gauss(0,0.1));
    b = [random.gauss(0,0.1)];
    
    cal_len = len(chis_data);
    for i in range(n,cal_len):
        x = chis_data[i-n:i];
        py = front_out(w,b,x);
        y = chis_data[i];
#         print py,y;
#         print w,b;
        change(w,b,x,py-y,lr);
        
        
    for rept in range(date_range_size):
        cal_len = len(chis_data);
        tmpn=0;
        predict=0.0;
        x = chis_data[cal_len-n:];
        y = []
        predict = front_out(w, b, x);
        #change(w,b,x,predict-y,lr);
        
        noise = random.gauss(0,sigma);
        predict = int(math.ceil(predict*1.0+noise));
        diff.append(predict);
        predict = predict+chis_data[-1];
        # chis_data.append(predict+chis_data[-1]);
        result.append(predict);
    return result;


def predict_model6(his_data,# 某种类型的虚拟机的历史数据
                   date_range_size):# 需要预测的长度

    '''
    预测方案六,使用SMV模型预测，添加正态随机噪声 全部数据  
    历史长度为n个粒度时间，权重设定暂定，
    his_data:['time':[时间标签],'value':[值]]
    '''
    
    
    n =  7; # 历史长度
    sigma = 0.01;
    
    n_layer1 = 2;
    chis_data = copy.deepcopy(his_data['value']);
    cal_len = len(chis_data);
    avag = [];
    tmp=0.0;
    last=0.0;
    for i in range(n_layer1):
        last = chis_data[i]*1.0/n_layer1;
        tmp += last;
    avag.append(tmp);    
    for i in range(n_layer1,cal_len):
        tmp-= last;
        last = chis_data[i]*1.0/n_layer1;
        tmp += last;
        avag.append(tmp);

    
    result = [];
    for rept in range(date_range_size):
        cal_len = len(avag);
        tmpn=0;
        predict=0.0;
        for i in range(cal_len-1,-1,-1):
            predict+= avag[i];
            tmpn+=1;
            if tmpn==n:break;
        noise = random.gauss(0,sigma);
        predict = int(math.ceil(predict*1.0/tmpn+noise));
        avag.append(predict);
        result.append(predict);
    return result;

def predict_model7(his_data,# 某种类型的虚拟机的历史数据
                   date_range_size):# 需要预测的长度

    '''
    预测方案七,对若干星期前同一天数据求平均
    his_data:['time':[时间标签],'value':[值]]
    '''
    
    
    n =  2; # 星期周围数
    sigma = 0.000001;
    
    back_week = 4;
    chis_data = copy.deepcopy(his_data['value']);
    cal_len = len(chis_data);

    result = [];
    for rept in range(date_range_size):
        day_avage=0.0;
        cot=0;
        for i in range(1,back_week+1):
            index = i*7;
            if index<=cal_len:
                cot+=1;
                day_avage+=chis_data[-index];
                for j in range(1,n+1):
                    day_avage+=chis_data[-index+j];
                    cot+=1;
                    if index+j <= cal_len:
                        day_avage+=chis_data[-index-j];
                        cot+=1;
                    else:continue;
            else:break;
        day_avage = day_avage*1.0 / cot; # 注意报错
        
        noise = random.gauss(0,sigma);
        day_avage = int(math.ceil(day_avage+noise));
        chis_data.append(day_avage);        
        result.append(day_avage);    

    return result;






