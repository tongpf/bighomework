def play(stat,storage):
    return storage['is_safe'](stat,storage)

def load(stat,storage):
    from random import choice
    
    def set_track(stat,storage):
        storage['track']=[[]]
        
    def find_path(stat,storage,band):
        #band为所要去的条形区域[[]]
        path=[[]]
        return path
    
    def is_safe(stat,storage):
        if True:   #判断是否需要更新路径
            storage['set_track'](stat,storage)
        return choice('lrxxxx')
    
    storage['set_track']=set_track
    storage['find_path']=find_path
    storage['is_safe']=is_safe
