# -*- coding: utf-8 -*-
"""
Created on Fri Feb  2 17:29:29 2018

@author: liberalism
"""

"""
测试的Apriori算法
"""
from itertools import combinations #导入需要的包 
#初始的数据
data=[['a','b','c','d'],
      ['b','c','e'],
      ['a','b','c','e'],
      ['b','d','e'],
      ['a','b','c','d']]
minsupport=0.4  #最小支持度
def creat_c1(data): #该函数算出ck为C1，fg为L1
    ck=[]
    fg={}
    for item in data:
        for item1 in item:
            if isexsist(item1,ck):#判断在ck中是否存在item1这个元素，若存在则字典值加一
                fg[item1]=fg[item1]+1#不存在则添加到字典和元组中，初始值为1
                continue
            ck.append(item1)
            fg[item1]=1
    return ck,fg

def isexsist(item,ck):#判断在ck中是否有与item相等的项
    for k in ck:
        if item==k:
            return True
    return False

def creat_Lk(Lk,k,data):#算出Ck
    l=[]
    result_lk=[]
    c1,l1=creat_c1(data)
    l=list(combinations(c1,k))
    for x in l:
            if panduanhou(Lk,x):
                result_lk.append(x)
            else:pass
    #map(frozenset,l)
    #shiftlist(l)
    return result_lk
def panduanhou(l_1,em):#判断em中的元素重新组合成每项em的长度-1次（少一个）后的
    #result=[]每项是否在l_1中有出现
    sort=[]
    sort=list(combinations(em,len(em)-1))
    count=0
    for ite in l_1:
        for pro in sort:
            if list(pro)==list(ite):
                count=count+1
            else:pass
    #print(count)
    if count>=len(sort):
        return True   #若有出现返回true,否则false
    else:return False


def shiftlist(lis):#将列表的第一项元素转换为列表
    result=[]
    for i in lis:
        result.append(list(i))
    return result

#x,y=creat_c1(data)

def ap(C1,data):        #核心的算法，把所有方法集中在一块处理，算出各个可能，
    print("打印出所有的Lk")#打印在屏幕上
    di={}
    at=[]
    at.append(C1)
    for j in range(2,len(data)):
        ltest=[]
        ltest=creat_Lk(at[j-2],j,data)
        print("这是中间的CK:",at[j-2])
        for y in ltest:                       #==========================
            di[y]=0                           #此块内容用于扫描新组成的数组在
            for x in data:                    #data中的次数
                if set(y).issubset(x):        #
                    di[y]=di[y]+1             #
                else:pass                     #==========================
        ltestafter=delnot(ltest,di)    
        at.append(ltestafter)
        print("L"+str(j)+":",ltestafter)
        print("具体的数据Lk：",di)    
        di={}
        
def delnot(lists,dic):#删除小于最小支持度的项
    res=[]
    for x in lists:
        if dic[x]>=minsupport*len(data):
            res.append(x)
    return res


c,k=creat_c1(data)      #函数带入值
ap(c,data)              #run的出结果
        
            
        