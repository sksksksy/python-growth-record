# -*- coding: utf-8 -*-
"""
Created on Sat Mar 24 16:35:26 2018

@author: Uz
"""
import re,time
import requests
from bs4 import BeautifulSoup
class flimSpider():
  baseurl="http://www.ygdy8.net"
  indexurl="http://www.ygdy8.net/html/gndy/dyzz/list_23_%s.html"
  jieguo=[]
  def get_flim_mainfurl(self,page):#主函数，核心调度代码
      try:
          for i in range(1,page+1):
              uu="http://www.ygdy8.net/html/gndy/dyzz/list_23_"+str(i)+".html"
              docment=self.re_page(uu)
              #print(docment)
              url,name=self.analyzepage(docment)
              final_thumber_url=self.iterobject(url)
              #print(url)
              self.jieguo=self.format_url(name,final_thumber_url)
              #print(jieguo)
              time.sleep(1)
              #print("打印完第%s页链接"%i)
      except:
          print(">>unknow system error!!")
      finally:
          print("<<<<<<<<<<<电影的初始链接提取完毕>>>>>>>>>>>")
          
  def re_page(self,url):#请求网页的函数
      re1=requests.get(url)
      re1.encoding="GBK"
      return re1.text
  def analyzepage(self,doc):#分析取出进入每部电影单独的链接
      urls=[]
      title=[]
      soup=BeautifulSoup(doc,"html.parser") 
      links=soup.find_all("a",class_="ulink")
      for link in links:
          url1=self.baseurl+link.get("href")
          urls.append(url1)
          aa=link.text
          title.append(aa)         
      return urls,title  
  def analyflimthum(self,doc):#分析取出电影的ftp地址
      soup1=BeautifulSoup(doc,"html.parser") 
      furl=soup1.find("a",attrs={"href":re.compile(r"ftp://(.)*")})
      furl=furl.get("href")
      return str(furl)
  def iterobject(self,url_lists):#迭代函数，获得ftp地址
      reurl=[]
      try:
          for url_list in url_lists:
              iter_request=self.re_page(url_list)
              reurl.append(self.analyflimthum(iter_request))
              time.sleep(2)
      except:
          print("第二次取迅雷链接错误！！！")
      finally:
          print("run over......")
          return list(reurl) 
  def format_url(self,name,url):#格式函数，调整输入格式的
      results=[]
      try:
          for x in range(len(name)):
              results.append("电影名:"+name[x]+"迅雷链接:"+url[x])
      except:
          print("错误1....")
      finally:
          return results
       
if __name__=="__main__":
    fun=flimSpider()
    fun.get_flim_mainfurl(1)#1表示爬取1页的电影
    for x in fun.jieguo:#保存在文件中
        with open("E:\movegold.txt","a") as f:
            f.write(x+"\n")
    print(">>>>>保存成功..............>>>>>>>>>")
        