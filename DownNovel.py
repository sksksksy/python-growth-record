# -*- coding: utf-8 -*-
"""
Created on Sun Apr  1 19:58:52 2018

@author: Uz
"""
import requests,csv
from lxml import etree
import queue
u_agent={'User-Agent':'Mozilla/5.0(Macintosh;U;IntelMacOSX10_6_8;en-us)AppleWebKit/534.50(KHTML,likeGecko)Version/5.1Safari/534.50'}
from bs4 import BeautifulSoup
re=requests.get("http://book.zongheng.com/showchapter/675589.html",headers=u_agent)
'''http://book.zongheng.com/chapter/675589/36982942.html'''
re.encoding='utf-8'
#soup=BeautifulSoup(re.text,'html.parser')
#p=soup.find_all('td',attrs={'class':'chapterBean'})
html=etree.HTML(re.text)
novel_tds=html.xpath('.//td[@class="chapterBean"]')
content=[]
for td_a in novel_tds:
    diao={}
    href=td_a.xpath('./a/@href')[0].encode('utf-8')
    name=td_a.xpath('./a')[0].text
    #diao.append(name)
    #diao.append(bytes.decode(href))
    #content.append(diao)
    diao['url']=bytes.decode(href)
    diao['chapter']=name
    content.append(diao)
print("所有章节信息下载完毕.........")
head=['chapter','url']
with open('novel_info.csv','w') as f:
    fc=csv.DictWriter(f,head)
    fc.writeheader()
    fc.writerows(content)
print("正在下载相关章节内容.........")
url_queue=queue.Queue()
name_queue=queue.Queue()
with open('novel_info.csv','r') as fr:
    fcs=csv.DictReader(fr)
    for row in fcs:
        url_queue.put(row.get('url'))
        name_queue.put(row.get('chapter'))
        
def downText(url):
    nie=[]
    rr=requests.get(url,headers=u_agent)
    rr.encoding='utf-8'
    #htm=etree.HTML(rr.text)
    #contents=htm.xpath('./div[@id="readerFs"]//p')
    so=BeautifulSoup(rr.text,'html.parser')
    tt=so.find_all('div',attrs={'id':'readerFs'})
    ht=etree.HTML(str(tt[0]))
    for content in ht.xpath('//p'):
        nie.append(content.text+"\n")
    return nie
    
def save_novel(nie,name):
    title=name+'.txt'
    with open(title,'w') as f:
        f.write(nie)
    print("%s保存成功"%name)
def diaokong():
    #while url_queue.get()==None:
    for i in range(3):
        D_text1=downText(url_queue.get())
        D_text="".join(D_text1)
        save_novel(D_text,name_queue.get())
    print("all over......")
if __name__=='__main__':
    diaokong()
"""
保存文件和下载文件有些小Bug"""