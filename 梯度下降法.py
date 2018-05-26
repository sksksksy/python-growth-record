# -*- coding: utf-8 -*-
"""
Created on Fri May 25 15:10:22 2018

@author: Administrator
"""
import matplotlib.pyplot as plt

"""
x=[1,2,3,4,5,6,7,8]
y=[1,2,3,4,5,6,7,8]
w=[0,0]
w表示待学习的参数
"""
def han(w1,xi):
    re=0
    #for i in range(2):
    #    re=re+w1[i]*xi
    re=w1[0]+w1[1]*xi
    return re
def jian(w2,x3,y3):
    x0=[]
    #x1=[]
    for i in range(8):
        x0.append(han(w2,x3[i])-y3[i])
    return x0
def xaingliang(x1,y1):
    n=0
    for i in range(8):
       n=n+x1[i]*y1[i]
    return n
       
def tidu(w3,x2,y2):
    alp=0.001
    xx=[0 for _ in range(0,8)]
    nw=[]
    for i in range(2):
        if i==0:    
            nw.append(w3[i]-alp*xaingliang(jian(w3,x2,y2),xx))
        else:
            nw.append(w3[i]-alp*xaingliang(jian(w3,x2,y2),x2))
    return nw
def hh(w0,x0):
    y0=[]
    for xi in x0:
        y0.append(han(w0,xi))
    return y0

print("start ....")
i=0
x=[1,2,3,4,4.8,6,7,8]
y=[2,4,6,8,10,12,14,17]
w=[0,0]
while True:
    i=i+1
    w=tidu(w,x,y)
    #print(w)
    if i==10000:#(han(w,5)-5)<0.5:
        print(w)
        break
x1=[ i for i in range(9)]
plt.plot(x,y,'mo:',x1,hh(w,x1),'r--')
plt.show()
print("end...")