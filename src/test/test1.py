# -*- coding: utf-8 -*-
'''
Created on 2018年3月9日

@author: zwp
'''

split_append_tmp=[[13,':00:00'],[10,' 00:00:00']];
def get_grain_time(time_str,time_grain):
    sp_len_tmp = split_append_tmp[time_grain][0];
    sp_str_tmp = split_append_tmp[time_grain][1];
    return time_str[:sp_len_tmp]+sp_str_tmp;


if __name__ == '__main__':
    print 'hello world'
    print get_grain_time('2015-02-18 11:05:34',0);
    print get_grain_time('2015-02-15 02:05:34',1);
    
    a = {};
    print 'a' in a.keys();
    a['a']='b';
    print 'a' in a.keys();
    
    b = [1,2,3,4];
    print b.index(1);
    
    for index in range(3,-1,-1):
        print(index);
        print('v',b[index]);
    print index;
    pass;

