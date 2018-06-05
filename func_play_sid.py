'''
函数注释模板：
函数说明：对函数功能进行简单的陈述，便于后续快速知道该函数的功能
传入参数：
    参数名 参数类型    参数的说明   举例：
    band    list[list]  二维列表，是场地的纸带属性。
返回：
    返回值 返回类型    返回的说明   举例：
    path    list[list]  二维列表，到指定区域的路径
version:
    1.0:    date:2018/6/4   by '作者名'    本次版本更新内容变动。也可以记一些辅助的文字帮助下次编写。

'''


def play(stat,storage):
    '''
    函数说明：一个建议模板。
    传入参数：
        stat
        storage
    返回：
        'left' or 'right' or 'straight' 返回转向指令，即 左转|右转|直行
    version:
        1.0:    date:2018/6/5   by sid  对play函数模板的一些看法。主要是play中函数调用可以更简单，对函数参数接口要求可以更明确。增加对函数的注释的模板。
    '''
    return is_safe(stat,storage) 

def load(stat,storage):
    from random import choice
    
    def set_track(stat,storage):
        '''
        函数说明：更新圈地路径
        传入参数：
            stat
            storage
        返回：
            list[list]  二维列表，路径的位置为1，不为路径的位置为0
        version:
            by st
        '''
        return track
        
    def find_path(stat,storage,band):
        '''
        函数说明：找到去某一条形区域的路径
        传入参数：
            stat
            storage
            band:   list[list]  二维列表，为所要去的条形区域。
        返回：
            path    list[list]  二维列表，为去指定区域的路径
        version:
            by Tong
        '''
        return path
    
    def is_safe(stat,storage):
        '''
        函数说明：一个功能很多的函数
        传入函数：
            stat
            storage
        返回：
            'left' or 'right' or 'straight' 返回转向指令，即 左转|右转|直行
        version:
            by sid
            
        '''
        if True:   #判断是否需要更新路径
            storage['set_track'](stat,storage)
        return choice('lrxxxx')
    
