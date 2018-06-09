from timeit import Timer

def find_path(stat,operate='me_to_home',pathstat=None,pathmark=None,outputmark='mypath',myx=None,myy=None,myid='me'):
    '''
    寻路函数，寻找me/enemy到达各自领地，对方纸带，或给定路径的长度和路径
    传入参数：
        stat
        operate     字符串     默认me_to_home，支持me_to_home, me_to_path, enemy_to_home, enemy_to_path, site_to_home, custom
        pathstat    二维数组    默认None,自定义的路径信息，配合_to_path两operate使用
        pathmark    字符串     默认None,自定义路径信息中的路径标记
        outputmark  字符串     默认mypath,输出路径信息中的路径标记
    返回：
        outputpath   二维数组
        distance    字符串     路径长度
    版本：
        6.0：    童培峰
    存在问题：
        出现同样distance的不同路径时如何寻找最优解
    '''

    if operate == 'me_to_home':
        myid = stat['now']['me']['id']
        myx = stat['now']['me']['x']
        myy = stat['now']['me']['y']
        statlist = stat['now']['fields']
        fieldid = myid
    elif operate == 'enemy_to_home':
        myid = stat['now']['enemy']['id']
        myx = stat['now']['enemy']['x']
        myy = stat['now']['enemy']['y']
        statlist = stat['now']['fields']
        fieldid = myid
    elif operate == 'me_to_path':
        myid = stat['now']['me']['id']
        myx = stat['now']['me']['x']
        myy = stat['now']['me']['y']
        if not pathstat:
            statlist = stat['now']['bands']
            fieldid = stat['now']['enemy']['id']
        else:
            statlist = pathstat
            fieldid = pathmark
    elif operate == 'enemy_to_path':
        myid = stat['now']['enemy']['id']
        myx = stat['now']['enemy']['x']
        myy = stat['now']['enemy']['y']
        if not pathstat:
            statlist = stat['now']['bands']
            fieldid = stat['now']['me']['id']
        else:
            statlist = pathstat
            fieldid = pathmark
    elif operate == 'site_to_home':
        myid = stat['now']['me']['id']
        statlist = stat['now']['fields']
        fieldid = myid
    elif operate == 'custom':
        statlist = pathstat
        fieldid = pathmark

    outputpath = []
    col_length = stat['size'][0]
    row_length = stat['size'][1]
    #col_length = len(stat['now']['fields'])#可以用storage里的size替代
    #row_length = len(stat['now']['fields'][0])
    distance = col_length + row_length
    finalpath = []

    for x in range(col_length):
        outputpath.append([])
        for y in range(row_length):
            outputpath[x].append(None)
            #判断是不是领地范围
            if statlist[x][y] == fieldid:
                temp_distance = abs(x-myx) + abs(y-myy)#计算最短路径距离
                #判断距离是否更小
                if temp_distance <= distance:
                    #分四象限考虑
                    if x < myx and y < myy:#第二象限
                        #是不是边缘点
                        if statlist[x+1][y] != fieldid and statlist[x][y+1] != fieldid:#角落
                            path1 = [(outputmark,i,y) for i in range(x,myx) if stat['now']['bands'][i][y]!=myid]
                            path2 = [(outputmark,myx,j) for j in range(y,myy) if stat['now']['bands'][myx][j]!=myid]
                            path = path1 + path2
                            if len(path) == temp_distance:
                                distance = temp_distance
                                finalpath = path
                            else:
                                path1 = [(outputmark,x,j) for j in range(y,myy) if stat['now']['bands'][x][j]!=myid]
                                path2 = [(outputmark,i,myy) for i in range(x,myx) if stat['now']['bands'][i][myy]!=myid]
                                path = path1 + path2
                                if len(path) == temp_distance:
                                    distance = temp_distance
                                    finalpath = path
                        elif statlist[x+1][y] != fieldid:#同上一
                            path1 = [(outputmark,i,y) for i in range(x,myx) if stat['now']['bands'][i][y]!=myid]
                            path2 = [(outputmark,myx,j) for j in range(y,myy) if stat['now']['bands'][myx][j]!=myid]
                            path = path1 + path2
                            if len(path) == temp_distance:
                                distance = temp_distance
                                finalpath = path
                        elif statlist[x][y+1] != fieldid:#同上二
                            path1 = [(outputmark,x,j) for j in range(y,myy) if stat['now']['bands'][x][j]!=myid]
                            path2 = [(outputmark,i,myy) for i in range(x,myx) if stat['now']['bands'][i][myy]!=myid]
                            path = path1 + path2
                            if len(path) == temp_distance:
                                distance = temp_distance
                                finalpath = path
                    elif x > myx and y < myy:#第一象限
                        if statlist[x-1][y] != fieldid and statlist[x][y+1] != fieldid:#角落
                            path1 = [(outputmark,i,y) for i in range(myx+1,x+1) if stat['now']['bands'][i][y]!=myid]
                            path2 = [(outputmark,myx,j) for j in range(y,myy) if stat['now']['bands'][myx][j]!=myid]
                            path = path1 + path2
                            if len(path) == temp_distance:
                                distance = temp_distance
                                finalpath = path
                            else:
                                path1 = [(outputmark,x,j) for j in range(y,myy) if stat['now']['bands'][x][j]!=myid]
                                path2 = [(outputmark,i,myy) for i in range(myx+1,x+1) if stat['now']['bands'][i][myy]!=myid]
                                path = path1 + path2
                                if len(path) == temp_distance:
                                    distance = temp_distance
                                    finalpath = path
                        elif statlist[x-1][y] != fieldid:
                            path1 = [(outputmark,i,y) for i in range(myx+1,x+1) if stat['now']['bands'][i][y]!=myid]
                            path2 = [(outputmark,myx,j) for j in range(y,myy) if stat['now']['bands'][myx][j]!=myid]
                            path = path1 + path2
                            if len(path) == temp_distance:
                                distance = temp_distance
                                finalpath = path
                        elif statlist[x][y+1] != fieldid:
                            path1 = [(outputmark,x,j) for j in range(y,myy) if stat['now']['bands'][x][j]!=myid]
                            path2 = [(outputmark,i,myy) for i in range(myx+1,x+1) if stat['now']['bands'][i][myy]!=myid]
                            path = path1 + path2
                            if len(path) == temp_distance:
                                distance = temp_distance
                                finalpath = path
                    elif x < myx and y > myy:#第三象限
                        if statlist[x+1][y] != fieldid and statlist[x][y-1] != fieldid:#角落
                            path1 = [(outputmark,i,y) for i in range(x,myx) if stat['now']['bands'][i][y]!=myid]
                            path2 = [(outputmark,myx,j) for j in range(myy+1,y+1) if stat['now']['bands'][myx][j]!=myid]
                            path = path1 + path2
                            if len(path) == temp_distance:
                                distance = temp_distance
                                finalpath = path
                            else:
                                path1 = [(outputmark,x,j) for j in range(myy+1,y+1) if stat['now']['bands'][x][j]!=myid]
                                path2 = [(outputmark,i,myy) for i in range(x,myx) if stat['now']['bands'][i][myy]!=myid]
                                path = path1 + path2
                                if len(path) == temp_distance:
                                    distance = temp_distance
                                    finalpath = path
                        elif statlist[x+1][y] != fieldid:#同上一
                            path1 = [(outputmark,i,y) for i in range(x,myx) if stat['now']['bands'][i][y]!=myid]
                            path2 = [(outputmark,myx,j) for j in range(myy+1,y+1) if stat['now']['bands'][myx][j]!=myid]
                            path = path1 + path2
                            if len(path) == temp_distance:
                                distance = temp_distance
                                finalpath = path
                        elif statlist[x][y-1] != fieldid:#同上二
                            path1 = [(outputmark,x,j) for j in range(myy+1,y+1) if stat['now']['bands'][x][j]!=myid]
                            path2 = [(outputmark,i,myy) for i in range(x,myx) if stat['now']['bands'][i][myy]!=myid]
                            path = path1 + path2
                            if len(path) == temp_distance:
                                distance = temp_distance
                                finalpath = path
                    elif x > myx and y > myy:#第四象限
                        if statlist[x-1][y] != fieldid and statlist[x][y-1] != fieldid:#角落
                            path1 = [(outputmark,i,y) for i in range(myx+1,x+1) if stat['now']['bands'][i][y]!=myid]
                            path2 = [(outputmark,myx,j) for j in range(myy+1,y+1) if stat['now']['bands'][myx][j]!=myid]
                            path = path1 + path2
                            if len(path) == temp_distance:
                                distance = temp_distance
                                finalpath = path
                            else:
                                path1 = [(outputmark,x,j) for j in range(myy+1,y+1) if stat['now']['bands'][x][j]!=myid]
                                path2 = [(outputmark,i,myy) for i in range(myx+1,x+1) if stat['now']['bands'][i][myy]!=myid]
                                path = path1 + path2
                                if len(path) == temp_distance:
                                    distance = temp_distance
                                    finalpath = path
                        elif statlist[x-1][y] != fieldid:
                            path1 = [(outputmark,i,y) for i in range(myx+1,x+1) if stat['now']['bands'][i][y]!=myid]
                            path2 = [(outputmark,myx,j) for j in range(myy+1,y+1) if stat['now']['bands'][myx][j]!=myid]
                            path = path1 + path2
                            if len(path) == temp_distance:
                                distance = temp_distance
                                finalpath = path
                        elif statlist[x][y-1] != fieldid:
                            path1 = [(outputmark,x,j) for j in range(myy+1,y+1) if stat['now']['bands'][x][j]!=myid]
                            path2 = [(outputmark,i,myy) for i in range(myx+1,x+1) if stat['now']['bands'][i][myy]!=myid]
                            path = path1 + path2
                            if len(path) == temp_distance:
                                distance = temp_distance
                                finalpath = path
                    elif x == myx and y < myy:
                        path = [(outputmark,myx,j) for j in range(y,myy) if stat['now']['bands'][myx][j]!=myid]
                        if len(path) == temp_distance:
                            distance = temp_distance
                            finalpath = path
                    elif x == myx and y > myy:
                        path = [(outputmark,myx,j) for j in range(myy+1,y+1) if stat['now']['bands'][myx][j]!=myid]
                        if len(path) == temp_distance:
                            distance = temp_distance
                            finalpath = path
                    elif x < myx and y == myy:
                        path = [(outputmark,i,y) for i in range(x,myx) if stat['now']['bands'][i][y]!=myid]
                        if len(path) == temp_distance:
                            distance = temp_distance
                            finalpath = path
                    elif x > myx and y == myy:
                        path = [(outputmark,i,y) for i in range(myx+1,x+1) if stat['now']['bands'][i][y]!=myid]
                        if len(path) == temp_distance:
                            distance = temp_distance
                            finalpath = path
                    else:
                        distance = 0
                        finalpath = []
    if distance == col_length+row_length and operate != 'custom':
        outputpath, distance, nextx, nexty=path_not_find(statlist,fieldid,outputmark,myx,myy,myid)
        outputpath[nextx][nexty] = outputmark
        return outputpath, distance+1
    else:
        for item in finalpath:
            outputpath[item[1]][item[2]]=item[0]
        return outputpath, distance

def path_not_find(pathstat,pathmark,outputmark,x,y,id):
    index = [1,-1]
    p=pathstat
    d=stat['size'][0]+stat['size'][1]
    for i in index:
        try:
            if stat['now']['bands'][abs(x+i)][abs(y)]!=id:
                tempp,tempd = find_path(stat,operate='custom',pathstat=pathstat,pathmark=pathmark,outputmark=outputmark,myx=abs(x+i),myy=abs(y),myid=id)
                if tempd <= d:
                    p = tempp
                    d = tempd
                    nextx = x+i
                    nexty = y
        except IndexError:
            pass
    for i in index:
        try:
            if stat['now']['bands'][abs(x)][abs(y+i)]!=id:
                tempp,tempd = find_path(stat,operate='custom',pathstat=pathstat,pathmark=pathmark,outputmark=outputmark,myx=abs(x),myy=abs(y+i),myid=id)
                if tempd <= d:
                    p = tempp
                    d = tempd
                    nextx = x
                    nexty = y+i
        except IndexError:
            pass
    return p, d, nextx, nexty


if __name__=='__main__':
    stat={}
    stat['now'] = {}
    me={}
    stat['now']['me']=me
    stat['now']['me']['id'] = 1
    stat['now']['me']['x'] = 4
    stat['now']['me']['y'] = 0
    enemy={}
    stat['now']['enemy']=enemy
    stat['now']['enemy']['id']=2
    stat['now']['enemy']['x']=2
    stat['now']['enemy']['y']=2
    fieldlist = [[1 for j in range(101)] for i in range(101)]
    #stat['now']['fields'] = fieldlist
    stat['now']['fields'] = [
    [0,0,0,0,0,0],
    [0,0,0,0,0,0],
    [0,0,0,1,1,0],
    [0,0,0,1,1,0],
    [0,0,0,0,0,0]]
    stat['now']['bands'] = [
    [0,0,0,0,0,0],
    [0,0,0,0,0,0],
    [0,1,1,0,0,0],
    [0,1,0,0,0,0],
    [1,1,0,0,0,0]]
    stat['size'] = [len(stat['now']['fields']),len(stat['now']['fields'][0])]
    #for i in range(10):
    finalpath, distance = find_path(stat,'me_to_home')
    t1 = Timer("find_path(stat,'me_to_home')","from __main__ import find_path,stat")
    print(t1.timeit(number=1))
    print(distance)
    for i in finalpath:
        print(i)
    #print(finalpath)
