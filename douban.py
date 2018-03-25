# -*- coding: utf-8 -*-
"""
Created on Sat Mar 24 13:59:52 2018

@author: Uz
"""
import requests
#from requests import Request
from bs4 import BeautifulSoup
class douban:
    url='https://movie.douban.com/chart'
    #def __init__(self):
        
    def anl(self):
        re=requests.get(self.url)
        re.enconding="utf-8"
        soup=BeautifulSoup(re.text,'html.parser')
        flimname=soup.find_all("span",style='font-size:13px;')
        flimpingfens=soup.find_all('span',class_="rating_nums")
        flimpr=soup.find_all("span",class_='box_chart_num color-gray')
        flimpingfen=list(flimpingfens)
        flimpr=list(flimpr)[2:]
        return flimname,flimpingfen,flimpr
    def save(self,doc):
        try:
            with open("E:\move.txt",'a') as f:
                f.write(doc)
            print("保存成功")
        except:
            print("system Error!!")
        finally:
            print("run over.....")
    def run(self):
        x1,x2,x3 = self.anl()
        a1=min(len(x1),len(x2),len(x3))
        print(a1)
        for i in range(a1):
           # redoc.append("电影名："+x1[i].text+" "+"评分:"+x2[i].text+" "+"评论人数："+x3[i].text+"\n")
            self.save("电影名："+x1[i].text+" "+"评分:"+x2[i].text+" "+"评论人数："+x3[i].text+"\n")
            
if __name__=="__main__":
    a=douban()
    a.run()
           
        
            